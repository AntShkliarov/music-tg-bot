# Music Search Telegram Bot

A Telegram bot that helps users search for songs across multiple music streaming platforms including Spotify and SoundCloud. Get quick access to your favorite music with simple commands!

## Project Description

This Telegram bot allows users to:
- Search for songs across multiple music streaming platforms
- Get direct links to songs on Spotify and SoundCloud
- View song details including artist, album, and duration
- Share music easily with friends through Telegram

## Installation

1. Clone the repository

```bash
git clone git@github.com:AntShkliarov/music-tg-bot.git
cd music-tg-bot
```
Note: Project's built with uv, so you can use uv to run the project.

2. Install dependencies

```bash
uv pip install -r requirements.txt
```

3. Set up environment variables


Create a `.env` file in the root of the project and add the following variables:

```
TG_BOT_KEY=
``` 

OR 

Feel free to try out exisitng bot in Telegram [@chueeesh_bot](https://t.me/chueeesh_bot)

## Launch Commands

1. Start the bot

```bash
docker build -t music-bot . && docker run -it music-bot
```

2. Bot Commands in Telegram:
- `/start` - Initialize the bot
- `/search <song name>` - Search for a song
- `/help` - Display available commands

## Main Libraries Used

- `python-telegram-bot` - Core Telegram bot functionality
- `soundcloud-api` - SoundCloud API integration
- `python-dotenv` - Environment variables management
- `requests` - HTTP requests handling

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

If you encounter any problems or have suggestions, please open an issue in the repository.
