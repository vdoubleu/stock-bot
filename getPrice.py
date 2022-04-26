import requests

def get_data(ticker, key):
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={ticker}&apikey={key}&outputsize=compact"
    r = requests.get(url)
    data = r.json()
    print(data)

    reversed_data = {date: data['Time Series (Daily)'][date] for date in reversed(data['Time Series (Daily)'])}

    return reversed_data


def get_index(ticker, num_days_from_today):
    data = get_data(ticker)

    # take last n entries
    last_days = data.items()[-num_days_from_today:]

    dict_form = {date: data for (date, data) in last_days}
    return dict_form
