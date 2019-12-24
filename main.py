from yahoofinance.graph.Dataplot import plot_hist_data
from yahoofinance.query.MultiDataRequest import get_multi_hist_data


if __name__ == '__main__':
    tickers = ['AAPL', 'MSFT', 'JPM']
    result = get_multi_hist_data(tickers)
    fields = ['Open', 'Close*']
    plot_hist_data(result, fields, tickers, nRows=1, nCols=2)

