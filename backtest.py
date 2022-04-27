from getPrice import get_data, get_index
from calc import update_shares_Kelly, update_shares_RSIprop
from allMetrics import init_metrics, update_metrics, get_metrics
import matplotlib.pyplot as plt
from key import API_KEY
from getTickers import get_tickers

def getPercDiff(init, curr):
    return ((curr - init) / init) * 100

def backtest(dataset_by_day, index_dataset_by_day, ticker, skip_n):
    shares_Kelly = 0
    shares_RSIprop = 0
    cash_init_amount = 10000
    cash_Kelly = cash_init_amount
    cash_RSIprop = cash_init_amount

    metrics = init_metrics(ticker, API_KEY)

    stock_prices = []
    index_prices = []
    net_worths_Kelly = []
    net_worths_RSIprop = []


    stock_init_price = None 
    index_init_price = None

    ind = 0
    for date in dataset_by_day:
        if ind < skip_n:
            ind += 1
            continue
        data_for_date = dataset_by_day[date]

        if stock_init_price is None:
            stock_init_price = float(data_for_date['4. close'])
        if index_init_price is None:
            index_init_price = float(index_dataset_by_day[date]['4. close'])

        stock_day_data = {
            'index': ind,
            'date': date,
            'open': float(data_for_date['1. open']),
            'high': float(data_for_date['2. high']),
            'low': float(data_for_date['3. low']),
            'close': float(data_for_date['4. close']),
            'volume': float(data_for_date['5. volume'])
        }

        stock_prices.append(getPercDiff(stock_init_price, stock_day_data['close']))
        index_prices.append(getPercDiff(index_init_price, float(index_dataset_by_day[date]['4. close'])))
        net_worths_Kelly.append(getPercDiff(cash_init_amount, cash_Kelly + (shares_Kelly * stock_day_data['close'])))
        net_worths_RSIprop.append(getPercDiff(cash_init_amount, cash_RSIprop + (shares_RSIprop * stock_day_data['close'])))
        

        update_metrics(metrics, stock_day_data)

        [cash_Kelly, shares_Kelly] = update_shares_Kelly(shares_Kelly, cash_Kelly, stock_day_data, get_metrics(metrics))
        [cash_RSIprop, shares_RSIprop] = update_shares_RSIprop(shares_RSIprop, cash_RSIprop, stock_day_data, get_metrics(metrics))
        ind += 1

    plt.plot(stock_prices)
    plt.plot(index_prices)
    plt.plot(net_worths_Kelly)
    plt.plot(net_worths_RSIprop)
    plt.xlabel('# of days')
    plt.ylabel('% difference')
    plt.legend(['Stock', 'Index (S&P 500)', 'Net Worth (Kelly)', 'Net Worth (RSI Prop)'])
    plt.title(ticker)
    plt.show()


if __name__ == "__main__":
    stock_tickers = get_tickers()
    stock_tickers = ['F', 'GOOG']
    for ticker in stock_tickers:
        dataset_by_day = get_data(ticker, API_KEY)
        index = get_data('SPY', API_KEY)
        backtest(dataset_by_day, index, ticker, 0)
