import matplotlib.pyplot as plt

from yahoofinance.query.MultiDataRequest import get_multi_hist_data


def plot_hist_data(data: dict, fields, tickers, nRows=1, nCols=1, titles=None):
    """
    :param data: The data to plot. Should be a dictionary where the keys are the tickers and the values are an element
        that can be subscripted using the field values (such as a pandas dataframe)
    :param fields: The fields whose values we are plotting
    :param tickers: The tickers whose fields we are plotting
    :param nRows: (Optional) The number of rows to have in one plot window (i.e 3 rows and 1 column
        would have the plots below one another)
    :param nCols: (Optional) The number of columns to have in one plot window (i.e 1 row and 3 columns
    would place the plots beside each other)
    :param titles: (Optional) Custom titles to be used for the plots. If not specified, the names of the fields will
        be used to label plots.
    :return: None
    """
    if nRows < 1:
        raise ValueError('The number of rows must be 1 or more')
    if nCols < 1:
        raise ValueError('The number of cols must be 1 or more')
    if titles is not None and len(fields) != len(titles):
        raise ValueError('The number of custom titles must match the number of fields!')

    fig, axes = plt.subplots(nrows=nRows, ncols=nCols)
    row_at = 0
    col_at = 0
    for i, field in enumerate(fields):
        if nRows > 1 and nCols > 1:
            ax = axes[row_at][col_at]
        elif nRows > 1:
            ax = axes[row_at]
        elif nCols > 1:
            ax = axes[col_at]
        else:
            ax = axes
        for ticker in tickers:
            data[ticker][field].astype(float).plot(ax=ax)

        ax.legend(tickers)
        if titles:
            ax.title.set_text(titles[i])
        else:
            ax.title.set_text(field)

        col_at += 1
        if col_at == nCols:
            row_at += 1
            col_at = 0
            if row_at >= nRows and i != len(fields) - 1:
                fig, axes = plt.subplots(nrows=nRows, ncols=nCols)
                row_at = 0

    plt.show()


if __name__ == '__main__':
    tickers = ['GOOG', 'AAPL', 'MSFT', "JPM"]
    fields = ['Open', 'High', 'Low']
    result = get_multi_hist_data(tickers)
    plot_hist_data(result, fields, tickers, nRows=1, nCols=2)
