from strategies.utils import *

class Kelly():
    def __init__(self, starting_cash):
        self.name = "kelly"
        self.shares_owned = 0
        self.cash = starting_cash
        pass

    def update(self, stock_day_data, metrics):
        kelly_crit = metrics['kelly_crit']
        stock_price = stock_day_data['close']
        prop = max(min(kelly_crit / 1.5, 1), -1) if kelly_crit else 0

        if prop > 0:
            amount_available_to_buy = (self.cash / stock_price)

            amount_to_buy = prop * amount_available_to_buy

            # print("buy", index, rsi, amount_to_buy, self.shares_owned, self.cash, stock_day_data['close'])
            return buy(self.shares_owned, amount_to_buy, self.cash, stock_day_data['close'])
        elif prop < 0:
            amount_available_to_sell = self.shares_owned

            amount_to_sell = -1 * prop * amount_available_to_sell

            # print("sell", index, rsi, amount_to_sell, self.shares_owned, self.cash, stock_day_data['close'])
            return sell(self.shares_owned, amount_to_sell, self.cash, stock_day_data['close'])
        else:
            return [self.cash, self.shares_owned]

