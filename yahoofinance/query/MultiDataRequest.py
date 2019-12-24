import logging as data_logging
import multiprocessing
import time
from collections import deque
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed
from threading import BoundedSemaphore

import pandas as pd
from bs4 import BeautifulSoup, SoupStrainer

from yahoofinance.query.DataRequest import HistDataRequest, MissingDataException, DataTimeoutError, DataFetchException
from .QueryUtils import Countdown, CountdownTime


def __is_numeric_string__(string: str) -> bool:
    non_digits = set([ch for ch in string if not ch.isdigit()])
    if len(non_digits) <= 2:
        ch = next((ch for ch in non_digits if ch != '.' if ch != ','), None)
        if ch is None:
            return string.count('.') <= 1
    return False


def __get_hist_data__(ticker) -> pd.DataFrame:
    table = BeautifulSoup(HistDataRequest(ticker).resp(), 'lxml', parse_only=SoupStrainer("table")).find('table')
    if table is None:
        raise MissingDataException(['<table>'])

    if table.find('thead') is None:
        missing = ['<thead>']
        if table.find('tbody') is None:
            missing.append('<tbody>')
        raise MissingDataException(missing)

    if table.find('tbody') is None:
        raise MissingDataException(['<tbody>'])

    heads = [th.text for th in table.find('thead').find_all('th')]
    if not len(heads):
        raise MissingDataException(['<th> in <thead>'])

    rows = table.find('tbody').find_all('tr')
    if not len(rows):
        raise MissingDataException(['<tr> in <tbody>'])

    data = dict()
    for tr in table.find('tbody').find_all('tr'):
        cells = tr.find_all('td')
        if len(cells) >= len(heads):
            for th, td in zip(heads, cells):
                val = td.text.replace(",", "") if __is_numeric_string__(td.text) else td.text
                if th in data:
                    data[th].appendleft(val)
                else:
                    data[th] = deque([val])

    if not len(data):
        raise MissingDataException(['<td> in <tr>'])

    return pd.DataFrame(data=data)


def __get__hist__data__control(ticker, sem: BoundedSemaphore, njobs: Countdown, timeout: float,
                               sleep_time: float, logger: data_logging.Logger):
    timer = CountdownTime(sleep_time)
    res = sem.acquire(timeout=timeout)
    ret = None
    if not res:
        logger.log(data_logging.ERROR, f'Error::Timeout For Ticker {ticker}')
        ret = DataTimeoutError(timeout, f'requesting historical data for ticker = {ticker}')
    else:
        try:
            ret = __get_hist_data__(ticker)
        except MissingDataException as missing:
            logger.log(data_logging.ERROR, f'Error::Missing data in response for Ticker {ticker}')

            ret = missing

    # sleep and cleanup
    njobs.dec_count()
    if not njobs.finished() and not isinstance(ret, DataFetchException):
        time_left = timer.time_left_sec()
        if time_left > 0:
            logger.log(data_logging.DEBUG, f'sleeping: {time_left} seconds.')
            time.sleep(time_left)
    sem.release()
    if isinstance(ret, DataFetchException):
        raise ret
    return ret


def get_multi_hist_data(tickers, timeout=360, sleep_time=3, nsimultaneous=multiprocessing.cpu_count(),
                        logging=False, failfast=True) -> dict:
    """
    :param tickers: List of stock symbols, representing the stocks to get historical data for
    :param timeout: How long the program should wait for a stock's historical data to become available before giving up.
        defaults to 1 minute.
    :param sleep_time: How long we should sleep between each data request. This is a suggestion, it may or may not be
        followed.
    :param nsimultaneous: How many data requests should be made simultaneously. Defaults to the number of cpus.
    :param logging: Whether we should print logging messages.
    :param failfast: Whether the entire operation should fail if fetching data for one of the tickers fails.
        If False, errors will be ignored, and the program will still try and fetch data for the other tickers.
        If logging is enabled, an error message will be logged. Defaults to True.
    :return: A dictionary where each key is one of the tickers given in the :parameter tickers, and where each value is
        a pandas dataframe of historical stock information.
    """
    logger = data_logging.getLogger(__name__)
    if logging:
        logger.setLevel(data_logging.DEBUG)
    else:
        logger.setLevel(data_logging.NOTSET)

    sem = BoundedSemaphore(nsimultaneous)
    hist_data = dict()
    nworkers = nsimultaneous if nsimultaneous <= multiprocessing.cpu_count() + 4 else multiprocessing.cpu_count() + 4
    with ThreadPoolExecutor(max_workers=nworkers) as executor:
        job_count = Countdown(len(tickers))
        future_map = {executor.submit(__get__hist__data__control, ticker, sem, job_count, timeout, sleep_time, logger):
                          ticker for ticker in tickers}
        for future in as_completed(future_map, timeout=timeout):
            try:
                hist_data[future_map[future]] = future.result()
            except DataFetchException as err:
                if failfast:
                    raise err
                else:
                    msg = f'Exception caught when fetching data for Ticker {future_map[future]}: {err}'
                    logger.log(data_logging.CRITICAL, msg)

    return hist_data
