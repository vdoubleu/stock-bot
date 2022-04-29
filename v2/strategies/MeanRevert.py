import backtrader as bt
import math

class MeanRevert(bt.Strategy):
    params = (
        ('rsiperiod', 5),
        ('ema_period', 5),
        ('holdmax', 5),
        ('maxstockinvest', 0.05),
    )

    def __init__(self) -> None:
        self.dataclose = { data._name: data for data in self.datas }
        self.dataRSI = { data._name: bt.indicators.RSI(data, period=self.params.rsiperiod, safediv=True) for data in self.datas }
        self.dataBollinger = { data._name: bt.indicators.BollingerBands(data, period=self.params.rsiperiod, devfactor=2) for data in self.datas }
        
        # self.dataEMA = { data._name: bt.indicators.EMA(data, period=self.params.emaperiod) for data in self.datas }

        self.orders = {}
        self.holdlength = {}

    def notify_order(self, order):
        if order.status in [order.Submitted, order.Accepted]:
            return

        if not order.alive():
            dorders = self.orders[order.data]
            ind = dorders.index(order)
            dorders[ind] = None

            if all(x is None for x in dorders):
                dorders[:] = []
        
    def buy_stock(self, data, name, curr_date, size):
        self.orders[data] = [self.buy(data=data)]
        print(f"{curr_date} {name} buy {self.orders[data][0].size}")
        self.holdlength[data] = 0

    def close_stock(self, data, name, curr_date):
        curr_order = self.close(data=data)
        self.orders[data].append(curr_order)
        print(f"{curr_date} {name} sell {curr_order.size}")
                 
    def short_stock(self, data, name, curr_date, size):
        self.orders[data] = [self.buy(data=data, size=-1)]
        print(f"{curr_date} {name} short {self.orders[data][0].size}")
        self.holdlength[data] = 0

    def next(self):
        for ind, data in enumerate(self.datas):
            pos_size = self.getposition(data).size
            curr_date = self.datetime.date()
            name = data._name
            curr_cash = self.broker.get_cash()
            curr_value = self.broker.get_value()
            curr_amount_invested = curr_value - curr_cash
            max_investible_amount = curr_cash + 0.9 * curr_amount_invested
            max_number_of_stocks_buyable = max(1, math.floor(max_investible_amount / data.close[0]))
            amount_to_buy = max(1, math.floor(max_number_of_stocks_buyable * 0.25))

            if not pos_size and not self.orders.get(data, None):
                if self.dataRSI[name][0] < 30:
                    if self.dataRSI[name][0] < 20:
                        self.buy_stock(data, name, curr_date)
                    elif self.dataclose[name][0] > self.dataBollinger[name].lines.top[0]:
                        self.buy_stock(data, name, curr_date)  
                elif self.dataRSI[name][0] > 85:
                    self.short_stock(data, name, curr_date)
            elif pos_size and pos_size > 0:
                self.holdlength[data] += 1
                buy_in_price = self.getposition(data).price
                if buy_in_price * 1.05 < self.dataclose[name][0]:
                    self.close_stock(data, name, curr_date)
                elif buy_in_price * 0.9 > self.dataclose[name][0]: # stop loss
                    self.close_stock(data, name, curr_date)
                elif self.holdlength[data] >= self.params.holdmax:
                    self.buy_stock(data, name, curr_date)
            elif pos_size and pos_size < 0:
                self.holdlength[data] += 1
                buy_in_price = self.getposition(data).price
                if buy_in_price * 0.95 > self.dataclose[name][0]:
                    self.close_stock(data, name, curr_date)
                elif buy_in_price * 1.02 < self.dataclose[name][0]: #stop loss
                    self.close_stock(data, name, curr_date)
        pass