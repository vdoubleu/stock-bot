from metrics.baseAVReqIndicator import BaseAVReqIndicator

FUNC_NAME = 'RSI'
DEFAULT_VAL = 50

class RSI(BaseAVReqIndicator):
    def __init__(self, time_period, ticker, API_KEY):
        super().__init__(FUNC_NAME, ticker, API_KEY)
        self.data = self.av_request({'time_period': time_period})['Technical Analysis: ' + FUNC_NAME]
        self.curr_date = None

    def update(self, data):
        self.curr_date = data['date']

    def get(self):
        if self.curr_date:
            if self.curr_date in self.data:
                return float(self.data[self.curr_date][FUNC_NAME])
            else:
                return DEFAULT_VAL
        else:
            return None

    def __str__(self):
        return str(self.get())

    def __repr__(self):
        return str(self.get())
