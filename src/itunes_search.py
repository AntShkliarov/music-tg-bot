import logging
import requests
from src.itunes_query_builder import ITunesQueryBuilder

logger = logging.getLogger(__name__)


class ItunesSearchHandler:
    """
    Itunes Search Handler
    """

    __url = "https://itunes.apple.com/search"

    def search(self, query: str, country: str = "US", lang: str = "en_us", **kwargs):
        """
        Search for a song in Itunes
        :param query: str - the query to search for
        :param country: str - the country to search in
        :param lang: str - the language to search in
        :param kwargs: dict - the list of additional arguments
        """
        query_builder = ITunesQueryBuilder()

        query_builder.term(query)
        query_builder.country(country)
        query_builder.lang(lang)

        for key, value in kwargs.items():
            query_builder.add_param(key, value)

        query = query_builder.build_query()

        response = requests.get(self.__url, params=query)
        return response.json()
