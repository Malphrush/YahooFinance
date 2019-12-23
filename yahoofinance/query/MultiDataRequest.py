import time
from collections import deque
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed

import pandas as pd
from bs4 import BeautifulSoup, SoupStrainer

from yahoofinance.query.DataRequest import HistDataRequest


def __is_numeric_string__(string: str) -> bool:
    non_digits = set([ch for ch in string if not ch.isdigit()])
    if len(non_digits) <= 2:
        ch = next((ch for ch in non_digits if ch != '.' if ch != ','), None)
        if ch is None:
            return string.count('.') <= 1
    return False


def __get_hist_data__(ticker) -> pd.DataFrame:
    table = BeautifulSoup(HistDataRequest(ticker).resp(), 'lxml', parse_only=SoupStrainer("table")).find('table')
    data = dict()
    heads = [th.text for th in table.find('thead').find_all('th')]
    for tr in table.find('tbody').find_all('tr'):
        cells = tr.find_all('td')
        if len(cells) >= len(heads):
            for th, td in zip(heads, cells):
                val = td.text.replace(",", "") if __is_numeric_string__(td.text) else td.text
                if th in data:
                    data[th].appendleft(val)
                else:
                    data[th] = deque([val])

    return pd.DataFrame(data=data)


def get_multi_hist_data(tickers, timeout=360, sleep_time=3) -> dict:
    """
    :param tickers: List of stock symbols, representing the stocks to get historical data for
    :param timeout: How long the program should wait for a stock's historical data to become available before giving up.
        defaults to 1 minute.
    :param sleep_time: How long we should sleep between each data request. This is a suggestion, it may or may not be followed.
    :return: A dictionary where each key is one of the tickers given in the :parameter tickers, and where each value is
        a pandas dataframe of historical stock information.
    """
    hist_data = dict()
    with ThreadPoolExecutor() as executor:
        future_map = {executor.submit(__get_hist_data__, ticker): ticker for ticker in tickers}
        for future in as_completed(future_map, timeout=timeout):
            hist_data[future_map[future]] = future.result()
        time.sleep(sleep_time)

    return hist_data
