import backtrader as bt
from add_data_feeds import add_data
from strategies.RSI import RSIStrat

if __name__ == "__main__":
    cerebro = bt.Cerebro()
    cerebro.broker.set_cash(10000)

    add_data(cerebro)

    cerebro.addstrategy(RSIStrat, rsiperiod=5)
    
    print(f"starting value: {cerebro.broker.get_value()}")
    cerebro.run()

    print(f"ending value: {cerebro.broker.get_value()}")

    cerebro.plot()