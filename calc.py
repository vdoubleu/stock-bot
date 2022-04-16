def buy(shared_owned, amount_to_buy, cash, price):
    return [cash - amount_to_buy * price, shared_owned + amount_to_buy]

def sell(shares_owned, amount_to_sell, cash, price):
    return [cash + amount_to_sell * price, shares_owned - amount_to_sell]


def update_shares_owned(shares_owned, cash, stock_day_data, metrics):
    # this is where you add the logic to determine how much to buy/sell/hold


    return shares_owned
