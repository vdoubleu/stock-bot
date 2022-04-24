def buy(shares_owned, amount_to_buy, cash, price):
    return [cash - amount_to_buy * price, shares_owned + amount_to_buy]

def sell(shares_owned, amount_to_sell, cash, price):
    return [cash + amount_to_sell * price, shares_owned - amount_to_sell]

def RSI_prop(shares_owned, cash, stock_day_data, metrics):
    rsi = metrics['rsi']

    stock_price = stock_day_data['close']

    if rsi < 30:
        amount_available_to_buy = (cash / stock_price)

        prop = ((30 - rsi) / 30)
        amount_to_buy = prop * amount_available_to_buy

        return buy(shares_owned, amount_to_buy, cash, stock_day_data['close'])
    elif rsi > 70:
        amount_available_to_sell = shares_owned

        prop = ((rsi - 70) / 30)
        amount_to_sell = prop * amount_available_to_sell

        return sell(shares_owned, amount_to_sell, cash, stock_day_data['close'])
    else:
        return [cash, shares_owned]

def MA_prop(shares_owned, cash, stock_day_data, metrics):
    return [cash, shares_owned]

def update_shares_owned(shares_owned, cash, stock_day_data, metrics):
    # this is where you add the logic to determine how much to buy/sell/hold
    return RSI_prop(shares_owned, cash, stock_day_data, metrics)
    # return MA_prop(shares_owned, cash, stock_day_data, metrics)

