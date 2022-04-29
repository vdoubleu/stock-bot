import backtrader as bt
from add_data_feeds import add_data
from strategies.MeanRevert import MeanRevert

if __name__ == "__main__":
    start_cash = 10000

    cerebro = bt.Cerebro()
    cerebro.broker.set_cash(start_cash)

    stocks_added = add_data(cerebro)

    cerebro.addstrategy(MeanRevert, rsiperiod=5, maxstockinvest=1/stocks_added)
    
    print(f"starting value: {cerebro.broker.get_value()}")
    cerebro.run()

    print(f"ending value: {cerebro.broker.get_value()}")

    cerebro.plot()