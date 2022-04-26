from getPrice import get_data, get_index
from calc import update_shares_RSIkelly, update_shares_RSIprop
from allMetrics import init_metrics, update_metrics, get_metrics
import matplotlib.pyplot as plt
from key import API_KEY

def getPercDiff(init, curr):
    return ((curr - init) / init) * 100

def backtest(dataset_by_day, index_dataset_by_day, ticker, skip_n):
    shares_RSIkelly = 0
    shares_RSIprop = 0
    cash_init_amount = 10000
    cash_RSIkelly = cash_init_amount
    cash_RSIprop = cash_init_amount

    metrics = init_metrics(ticker, API_KEY)

    stock_prices = []
    index_prices = []
    net_worths_RSIkelly = []
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
        net_worths_RSIkelly.append(getPercDiff(cash_init_amount, cash_RSIkelly + (shares_RSIkelly * stock_day_data['close'])))
        net_worths_RSIprop.append(getPercDiff(cash_init_amount, cash_RSIprop + (shares_RSIprop * stock_day_data['close'])))
        

        update_metrics(metrics, stock_day_data)

        [cash_RSIkelly, shares_RSIkelly] = update_shares_RSIkelly(shares_RSIkelly, cash_RSIkelly, stock_day_data, get_metrics(metrics))
        [cash_RSIprop, shares_RSIprop] = update_shares_RSIprop(shares_RSIprop, cash_RSIprop, stock_day_data, get_metrics(metrics))
        ind += 1

    plt.plot(stock_prices)
    plt.plot(index_prices)
    plt.plot(net_worths_RSIkelly)
    plt.plot(net_worths_RSIprop)
    plt.xlabel('# of days')
    plt.ylabel('% difference')
    plt.legend(['Stock', 'Index (S&P 500)', 'Net Worth (RSI Kelly)', 'Net Worth (RSI Prop)'])
    plt.title(ticker)
    plt.show()


if __name__ == "__main__":
    stock_tickers = ['GOOG', 'MSFT']
    for ticker in stock_tickers:
        dataset_by_day = get_data(ticker, API_KEY)
        index = get_data('SPY', API_KEY)
        backtest(dataset_by_day, index, ticker, 0)
