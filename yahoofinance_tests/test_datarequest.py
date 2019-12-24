import pytest

from yahoofinance.query.DataRequest import *


def test_data_fetch_exception_extends_exception():
    data_fetch = DataFetchException()
    assert (isinstance(data_fetch, Exception))


@pytest.mark.parametrize("ticker", ['GOOG', 'AAPL', 'MSFT'])
def test_hist_data_req_init(ticker):
    data_req = HistDataRequest(ticker)
    assert data_req.invalid


@pytest.mark.parametrize("ticker", ['GOOG', 'AAPL', 'MSFT'])
def test_hist_data_valid_get(ticker):
    data_req = HistDataRequest(ticker)
    result = data_req.resp()
    assert (isinstance(result, bytes))
    assert (not data_req.invalid)


@pytest.mark.parametrize("ticker", ['GOOG', 'AAPL', 'MSFT'])
def test_hist_data_valid_get_string(ticker):
    data_req = HistDataRequest(ticker)
    result = data_req.resp_as_str()
    assert (isinstance(result, str))
    assert (not data_req.invalid)


@pytest.mark.parametrize("ticker", ["this/doesn't/exists", 'bad//url', '/dont/go/here',
                                    'does/not/exists', '/unknown/url/'])
def test_hist_data_bad_get(ticker):
    data_req = HistDataRequest(ticker)
    with pytest.raises(DataFetchException):
        data_req.resp()
    assert data_req.invalid


@pytest.mark.parametrize("ticker", ["this/doesn't/exists", 'bad//url', '/dont/go/here',
                                    'does/not/exists', '/unknown/url/'])
def test_hist_data_bad_get(ticker):
    data_req = HistDataRequest(ticker)
    with pytest.raises(DataFetchException):
        data_req.resp_as_str()
    assert data_req.invalid


@pytest.mark.parametrize("ticker", ['GOOG', 'AAPL', 'MSFT'])
def test_hist_data_get_accounts_for_invalid(ticker):
    data_req = HistDataRequest(ticker)
    data_req.resp()
    assert (not data_req.invalid)
    data_req.invalid = True
    data_req.resp()
    assert (not data_req.invalid)
