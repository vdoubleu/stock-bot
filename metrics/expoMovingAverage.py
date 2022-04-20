from baseAVReqIndicator import BaseAVReqIndicator

class ExpoMovingAverage(BaseAVReqIndicator):
    def __init__(self, time_period, smoothing=2, ticker):
        BaseAVReqIndicator.__init__("EMA", ticker)

        pass

    def update(self, data):
        pass

    def get(self):
        pass

    def __str__(self):
        return str(self.get())

    def __repr__(self):
        return str(self.get())
