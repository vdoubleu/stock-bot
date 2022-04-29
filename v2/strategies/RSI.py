import backtrader as bt

class RSIStrat(bt.Strategy):
    params = (
        ('rsiperiod', 5),
        ('ema_period', 5),
        ('holdmax', 5),
    )

    def __init__(self) -> None:
        self.dataclose = { data._name: data for data in self.datas }
        self.dataRSI = { data._name: bt.indicators.RSI(data, period=self.params.rsiperiod, safediv=True) for data in self.datas }
        self.dataBollinger = { data._name: bt.indicators.BollingerBands(data, period=self.params.rsiperiod, devfactor=2) for data in self.datas }
        
        
        #self.dataEMA = { data._name: bt.indicators.EMA(data, period=self.params.emaperiod) for data in self.datas }

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
        
    def buy_stock(self, data, name, curr_date):
        self.orders[data] = [self.buy(data=data)]
        print(f"{curr_date} {name} buy {self.orders[data][0].size}")
        self.holdlength[data] = 0

    def sell_stock(self, data, name, curr_date):
        curr_order = self.close(data=data)
        self.orders[data].append(curr_order)
        print(f"{curr_date} {name} sell {curr_order.size}")
                 
    def next(self):
        for ind, data in enumerate(self.datas):
            pos_size = self.getposition(data).size
            curr_date = self.datetime.date()
            name = data._name

            if not pos_size and not self.orders.get(data, None):
                if self.dataRSI[name][0] < 30:
                    if self.dataRSI[name][0] < 20:
                        self.buy_stock(data, name, curr_date)
                    elif self.dataclose[name][0] > self.dataBollinger[name].lines.top[0]:
                        self.buy_stock(data, name, curr_date)                    
            elif pos_size:
                self.holdlength[data] += 1
                buy_in_price = self.getposition(data).price
                if buy_in_price * 1.02 < self.dataclose[name][0]:
                    self.sell_stock(data, name, curr_date)
                elif buy_in_price * 0.9 > self.dataclose[name][0]:
                    self.sell_stock(data, name, curr_date)
                # elif self.holdlength[data] >= self.params.holdmax:
                #     self.sell_stock(data, name, curr_date)
                pass

        pass