import requests

class MovingAverage():
    def __init__(self, size, ticker, API_KEY):
        self.size = size
        self.data = []
        
        # url = f"https://www.alphavantage.co/query?function=SMA&symbol={ticker}&interval=daily&time_period={size}&series_type=close&apikey={API_KEY}"
        # r = requests.get(url)
        # data = r.json()
        # # reversed_data = {
        # #         date: data['Time Series (Daily)'][date] 
        # #         for date in reversed(data['Time Series (Daily)'])
        # #     }
        # # print(data)


        self.data = []

    def update(self, data):
        self.add(data['close'])

    def get(self):
        return sum(self.values) / len(self.values)

    def add(self, value):
        self.values.append(value)

        if len(self.values) > self.size:
            self.values.pop(0)

    def reset(self):
        self.values = []

    def __str__(self):
        return str(self.get())

    def __repr__(self):
        return str(self.get())


