def buy(shares_owned, amount_to_buy, cash, price):
    return [cash - amount_to_buy * price, shares_owned + amount_to_buy]

def sell(shares_owned, amount_to_sell, cash, price):
    return [cash + amount_to_sell * price, shares_owned - amount_to_sell]

def kelly(shares_owned, cash, stock_day_data, metrics):
    kelly_crit = metrics['kelly_crit']
    stock_price = stock_day_data['close']
    prop = max(min(kelly_crit / 1.5, 1), -1) if kelly_crit else 0

    if prop > 0:
        amount_available_to_buy = (cash / stock_price)

        amount_to_buy = prop * amount_available_to_buy

        # print("buy", index, rsi, amount_to_buy, shares_owned, cash, stock_day_data['close'])
        return buy(shares_owned, amount_to_buy, cash, stock_day_data['close'])
    elif prop < 0:
        amount_available_to_sell = shares_owned

        amount_to_sell = -1 * prop * amount_available_to_sell

        # print("sell", index, rsi, amount_to_sell, shares_owned, cash, stock_day_data['close'])
        return sell(shares_owned, amount_to_sell, cash, stock_day_data['close'])
    else:
        return [cash, shares_owned]

def RSI_kelly(shares_owned, cash, stock_day_data, metrics):
    rsi = metrics['rsi']
    kelly_crit = metrics['kelly_crit']
    date = stock_day_data['date']
    index = stock_day_data['index']

    stock_price = stock_day_data['close']

    # print(index, metrics)
    prop = max(min(kelly_crit / 2, 1), 0) if kelly_crit else 0

    if rsi < 30:
        amount_available_to_buy = (cash / stock_price)

        amount_to_buy = prop * amount_available_to_buy

        #print("buy", index, prop, amount_available_to_buy, shares_owned, cash, stock_day_data['close'])

        return buy(shares_owned, amount_to_buy, cash, stock_day_data['close'])
    elif rsi > 70:
        amount_available_to_sell = shares_owned

        amount_to_sell = prop * amount_available_to_sell

        #print("sell", index, prop, amount_available_to_sell, shares_owned, cash, stock_day_data['close'])
        return sell(shares_owned, amount_to_sell, cash, stock_day_data['close'])
    else:
        return [cash, shares_owned]


def RSI_prop(shares_owned, cash, stock_day_data, metrics):
    rsi = metrics['rsi']
    date = stock_day_data['date']
    index = stock_day_data['index']

    stock_price = stock_day_data['close']

    # print(index, metrics)

    if rsi < 30:
        amount_available_to_buy = (cash / stock_price)

        prop = ((30 - rsi) / 30)
        amount_to_buy = prop * amount_available_to_buy

        #print("buy", index, rsi, amount_to_buy, shares_owned, cash, stock_day_data['close'])
        return buy(shares_owned, amount_to_buy, cash, stock_day_data['close'])
    elif rsi > 70:
        amount_available_to_sell = shares_owned

        prop = ((rsi - 70) / 30)
        amount_to_sell = prop * amount_available_to_sell

        #print("sell", index, rsi, amount_to_sell, shares_owned, cash, stock_day_data['close'])
        return sell(shares_owned, amount_to_sell, cash, stock_day_data['close'])
    else:
        return [cash, shares_owned]

def MA_prop(shares_owned, cash, stock_day_data, metrics):
    return [cash, shares_owned]

def update_shares_RSIprop(shares_owned, cash, stock_day_data, metrics):
    return RSI_prop(shares_owned, cash, stock_day_data, metrics)

def update_shares_Kelly(shares_owned, cash, stock_day_data, metrics):
    return kelly(shares_owned, cash, stock_day_data, metrics)

# def update_shares_owned(shares_owned, cash, stock_day_data, metrics):
#     # return RSI_kelly(shares_owned, cash, stock_day_data, metrics)
#     # return RSI_prop(shares_owned, cash, stock_day_data, metrics)
#     return kelly(shares_owned, cash, stock_day_data, metrics)

