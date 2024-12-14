class ItunesResponseHandler:
    """
    Itunes Response Handler
    """

    def __init__(self, dict):
        self.__response_dict = dict

    def handle(self):
        if self.__response_dict["resultCount"] == 0:
            return "Song not found"
        else:
            return f"""
            Total results: {self.__response_dict['resultCount']}
            
            First song found: {self.__response_dict['results'][0]['trackName']} by {self.__response_dict['results'][0]['artistName']}\n
            Album: {self.__response_dict['results'][0]['collectionName']}\n
            Release date: {self.__response_dict['results'][0]['releaseDate']}\n
            Genre: {self.__response_dict['results'][0]['primaryGenreName']}\n
            Link: {self.__response_dict['results'][0]['trackViewUrl']}\n
            """
