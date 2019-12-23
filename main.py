from yahoofinance.graph.Dataplot import plot_hist_data
from yahoofinance.query.MultiDataRequest import get_multi_hist_data

if __name__ == '__main__':
    tickers = ['GOOG', 'AAPL', 'MSFT', "JPM"]
    fields = ['Open', 'High', 'Low']
    result = get_multi_hist_data(tickers)
    plot_hist_data(result, fields, tickers, nRows=1, nCols=3)
