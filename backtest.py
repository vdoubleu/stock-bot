from getPrice import get_data, get_index
from calc import update_shares_owned
from allMetrics import init_metrics, update_metrics, get_metrics
import matplotlib.pyplot as plt
from key import API_KEY

def getPercDiff(init, curr):
    return ((curr - init) / init) * 100

def getFirstDay(data):
    return next(iter(data))

def backtest(dataset_by_day, index_dataset_by_day, ticker):
    shares_owned = 0
    cash_init_amount = 10000
    cash = cash_init_amount

    metrics = init_metrics(ticker, API_KEY)

    stock_prices = []
    index_prices = []
    net_worths = []

    stock_init_price = float(dataset_by_day[getFirstDay(dataset_by_day)]['4. close'])
    index_init_price = float(index_dataset_by_day[getFirstDay(index_dataset_by_day)]['4. close'])

    for date in dataset_by_day:
        data_for_date = dataset_by_day[date]

        stock_day_data = {
            'date': date,
            'open': float(data_for_date['1. open']),
            'high': float(data_for_date['2. high']),
            'low': float(data_for_date['3. low']),
            'close': float(data_for_date['4. close']),
            'volume': float(data_for_date['5. volume'])
        }

        stock_prices.append(getPercDiff(stock_init_price, stock_day_data['close']))
        index_prices.append(getPercDiff(index_init_price, float(index_dataset_by_day[date]['4. close'])))
        net_worths.append(getPercDiff(cash_init_amount, cash + (shares_owned * stock_day_data['close'])))
        

        update_metrics(metrics, stock_day_data)

        [cash, shares_owned] = update_shares_owned(shares_owned, cash, stock_day_data, get_metrics(metrics))

    plt.plot(stock_prices)
    plt.plot(index_prices)
    plt.plot(net_worths)
    plt.legend(['Stock', 'Index', 'Net Worth'])
    plt.show()


if __name__ == "__main__":
    dataset_by_day = {}
    index = {}
    dataset_by_day = get_data('WMT', API_KEY)
    index = get_data('QQQ', API_KEY)
    backtest(dataset_by_day, index, 'WMT')
