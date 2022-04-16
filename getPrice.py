import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('AV_API_KEY')

def get_data(ticker):
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={ticker}&apikey={API_KEY}"
    r = requests.get(url)
    data = r.json()

    reversed_data = {date: data['Time Series (Daily)'][date] for date in reversed(data['Time Series (Daily)'])}

    return reversed_data


def get_index(ticker, num_days_from_today):
    data = get_data(ticker)

    # take last n entries
    last_days = data.items()[-num_days_from_today:]

    dict_form = {date: data for (date, data) in last_days}
    return dict_form
