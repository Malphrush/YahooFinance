from concurrent.futures import TimeoutError as ConcurrentTimeout

import pandas
import pytest

from yahoofinance.query.DataRequest import DataFetchException
from yahoofinance.query.MultiDataRequest import get_multi_hist_data


@pytest.fixture(scope="session")
def valid_fields():
    return ['Volume', 'Open', 'High', 'Low', 'Volume', 'Close*', 'Adj Close**']


@pytest.fixture(scope="session")
def tickers():
    return ['GOOG', 'JPM', 'MSFT', 'AAPL']


@pytest.fixture(scope="session")
def invalid_tickers():
    return ['DontExist', 'NotaTicker', 'IsNotATicker']


def test_get_multi_hist_data(valid_fields, tickers):
    result = get_multi_hist_data(tickers=tickers)
    assert (isinstance(result, dict))
    assert (len(result) == len(tickers))
    assert (set(key for key in result) == set(tickers))
    assert (all(isinstance(value, pandas.DataFrame) for value in result.values()))
    assert (all(field in value for field in valid_fields for value in result.values()))


def test_multi_hist_data_timeout(tickers):
    with pytest.raises(ConcurrentTimeout):
        nsimul = len(tickers) / 2
        if nsimul < 1:
            nsimul = 1
        result = get_multi_hist_data(tickers, timeout=0.1, sleep_time=100, nsimultaneous=nsimul, logging=True)


def test_get_multi_hist_data_failfast(tickers, invalid_tickers):
    with pytest.raises(DataFetchException):
        get_multi_hist_data(invalid_tickers + tickers, failfast=True)


def test_get_multi_hist_data_no_failfast(tickers, invalid_tickers):
    result = get_multi_hist_data(invalid_tickers + tickers, failfast=False)
    assert (len(result) == len(tickers))
