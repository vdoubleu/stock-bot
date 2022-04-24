def buy(shared_owned, amount_to_buy, cash, price):
    return [cash - amount_to_buy * price, shared_owned + amount_to_buy]

def sell(shares_owned, amount_to_sell, cash, price):
    return [cash + amount_to_sell * price, shares_owned - amount_to_sell]


def update_shares_owned(shares_owned, cash, stock_day_data, metrics):
    # this is where you add the logic to determine how much to buy/sell/hold

    rsi = metrics['rsi']

    stock_price = stock_day_data['close']

    if rsi < 30:
        amount_to_buy = int((cash / stock_price) / 5)
        return buy(shares_owned, amount_to_buy, cash, stock_day_data['close'])
    elif rsi > 70:
        amount_to_sell = int(shares_owned / 5)
        return sell(shares_owned, amount_to_sell, cash, stock_day_data['close'])
    else:
        return [cash, shares_owned]
