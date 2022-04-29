from metrics.baseAVReqIndicator import BaseAVReqIndicator

FUNC_NAME = 'EMA'

class ExpoMovingAverage(BaseAVReqIndicator):
    def __init__(self, time_period, ticker, API_KEY, smoothing=2):
        super().__init__(FUNC_NAME, ticker, API_KEY)

        self.data = self.av_request({'time_period': time_period})['Technical Analysis: ' + FUNC_NAME]
        self.curr_date = None
        pass

    def update(self, data):
        self.curr_date = data['date']
        pass

    def get(self):
        if self.curr_date:
            return float(self.data[self.curr_date][FUNC_NAME])
        else:
            return None

    def __str__(self):
        return str(self.get())

    def __repr__(self):
        return str(self.get())
