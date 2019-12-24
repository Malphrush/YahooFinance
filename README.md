# YahooFinance
Unofficial program for getting and plotting stock historical data from Yahoo Finance.
### Example:
```python
from yahoofinance.graph.Dataplot import plot_hist_data
from yahoofinance.query.MultiDataRequest import get_multi_hist_data

# define the stocks we want to get historical data for (Note: Only Ticker names are valid)
tickers = ['AAPL', 'MSFT', 'JPM']
# result will be a dictionary containing available historical data
result = get_multi_hist_data(tickers)
# Define the fields we want to plot. Available fields are (High, Low, Open, Volume, Close*, Adj Close**)
fields = ['Open', 'Close*']
# Plot the fields. nRows controls vertical stacking of plots, nCols horizontal.
# By defaults nRows = nCols = 1, and each field gets its own window (one plot per window)
plot_hist_data(result, fields, tickers, nRows=1, nCols=2)
```

![alt text](https://github.com/Malphrush/YahooFinance/blob/master/finance_example.JPG "Example Image 01")

Note: Data currently covers a 137 day period starting from the current date going backwards. 
