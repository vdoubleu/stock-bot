class BaseAVReqIndicator():
    def __init__(self, function, symbol):
        self.function = function
        self.symbol = symbol

    def av_request(self):
        url = f"https://www.alphavantage.co/query?function={self.function}&symbol={self.symbol}&interval=daily&time_period={size}&series_type=close&apikey={API_KEY}"
        r = requests.get(url)
        data = r.json()
        # reversed_data = {
        #         date: data['Time Series (Daily)'][date] 
        #         for date in reversed(data['Time Series (Daily)'])
        #     }
        # print(data)
