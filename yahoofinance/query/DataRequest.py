import requests as req
from requests.exceptions import HTTPError


class DataFetchException(Exception):
    def __init__(self, msg=""):
        super(DataFetchException, self).__init__(msg)


class HistDataRequest:
    base_url = 'https://finance.yahoo.com/quote/{}/history?p={}'

    def __init__(self, ticker):
        """
        :param ticker: the ticker to get historical data for
        """
        self.__url__ = self.base_url.format(ticker, ticker)
        self.__resp__ = None
        self.invalid = True

    def resp(self) -> bytes:
        """
        :return: returns the bytes of the HTTP response returned after requesting the stocks historical data
        """
        if self.invalid or self.__resp__ is None:
            response = req.get(self.__url__)
            try:
                response.raise_for_status()
            except HTTPError as httperr:
                raise DataFetchException(f"Failed to fetch data from url: {self.__url__}\n{httperr}")

            self.invalid = False
            self.__resp__ = response.content
            return self.__resp__
        else:
            return self.__resp__

    def resp_as_str(self, encoding="utf-8") -> str:
        """
        :param encoding: The encoding to use when decoding the response. Defaults to utf-8
        :return: returns a string version of the HTTP response returned after requesting the stocks historical data
        """
        result = self.resp()
        return result.decode(encoding)


if __name__ == "__main__":
    from bs4 import BeautifulSoup
    from bs4 import SoupStrainer

    soup = BeautifulSoup(HistDataRequest('GOOG').resp(), "lxml", parse_only=SoupStrainer('table'))
    print(soup.prettify())
