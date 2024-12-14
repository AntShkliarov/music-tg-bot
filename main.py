import os
import logging
import dotenv

from telegram import BotCommand, BotCommandScopeDefault, Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

from src.itunes_response_handler import ItunesResponseHandler
from src.itunes_search import ItunesSearchHandler

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

dotenv.load_dotenv()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await context.bot.send_message(
        chat_id=update.effective_chat.id, text=f"Hi {user.first_name} {user.last_name}!"
    )

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id, text="Enter song name to search for as '/search <song_name>'"  
    )

async def search(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id, text="Searching for song..."  
    )

    itunes_search_handler = ItunesSearchHandler()
    search_result = itunes_search_handler.search(query=update.message.text)

    answer = ItunesResponseHandler(search_result).handle()

    await context.bot.send_message(
        chat_id=update.effective_chat.id, text=answer
    )

if __name__ == "__main__":
    application = ApplicationBuilder().token(os.getenv("TG_BOT_KEY")).build()

    start_handler = CommandHandler("start", start)
    application.add_handler(start_handler)

    search_handler = CommandHandler("search", search)
    application.add_handler(search_handler)

    help_handler = CommandHandler("help", help)
    application.add_handler(help_handler)

    application.run_polling(allowed_updates=Update.ALL_TYPES)
