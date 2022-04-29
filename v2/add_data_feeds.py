import os
import datetime
import backtrader as bt

ignore_list = [
    # 'TSLA', 
    # 'DIS', 
    # 'JNJ', 
    # 'BRK-B', 
    # 'XOM',
    # 'AAPL',
    # 'F',
    # '^VIX',
    ]


def add_data(cerebro):
    # for file in data/ folder, add datafeed
    for file in os.listdir("data"):
        if (file.split(".")[0]) in ignore_list:
            continue
        data = bt.feeds.YahooFinanceCSVData(
            dataname=f"data/{file}",
            reverse=False, 
            fromdate=datetime.datetime(2019, 1, 1),
            plot=False
        )
        cerebro.adddata(data, name=file.split(".")[0])

        print(f"added data feed: {file}")