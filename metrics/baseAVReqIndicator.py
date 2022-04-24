import requests

class BaseAVReqIndicator():
    def __init__(self, function, symbol, API_KEY):
        self.function = function
        self.symbol = symbol
        self.API_KEY = API_KEY

    def av_request(self, other_params):
        def dic_to_params(dic):
            return '&'.join(['{}={}'.format(k, v) for k, v in dic.items()])

        url = f"https://www.alphavantage.co/query?function={self.function}&symbol={self.symbol}&interval=daily&series_type=close&apikey={self.API_KEY}&" + dic_to_params(other_params)

        r = requests.get(url)
        data = r.json()
        return data
