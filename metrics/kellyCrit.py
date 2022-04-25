from metrics.geoBrownian import GeoBrownian

class KellyCrit(GeoBrownian):
    def __init__(self, time_period):
        super().__init__()
        self.time_period = time_period

    def update(self, data):
        self.update_values(data)

    def get(self):
        if self.is_ready():
            drift = self.n_day_drift(self.time_period)
            volatility = self.n_day_volatility(self.time_period) 
            return drift / (volatility ** 2)
        else:
            return None
