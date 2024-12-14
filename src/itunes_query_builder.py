class ITunesQueryBuilder:
    """
    Itunes Query Builder
    """
    __query_params = dict()

    def build_query(self):
        query_params = self.__query_params.items()
        query = ""
        for key, value in query_params:
            query += f"{key}={value}&"
        return query

    def term(self, term: str):
        self.__query_params["term"] = term
        return self

    def media(self, media: str):
        self.__query_params["media"] = media
        return self
    
    def country(self, country: str):
        self.__query_params["country"] = country
        return self

    def lang(self, lang: str):
        self.__query_params["lang"] = lang
        return self
    
    def add_param(self, key: str, value: str):
        self.__query_params[key] = value
        return self

