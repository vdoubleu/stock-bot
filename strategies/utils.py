def buy(shares_owned, amount_to_buy, cash, price):
    return [cash - amount_to_buy * price, shares_owned + amount_to_buy]

def sell(shares_owned, amount_to_sell, cash, price):
    return [cash + amount_to_sell * price, shares_owned - amount_to_sell]

