from metrics.geoBrownian import GeoBrownian

class KellyCrit(GeoBrownian):
    def __init__(self, time_period_kelly, time_period_brownian):
        super().__init__(time_period_brownian)
        self.time_period_kelly = time_period_kelly

    def update(self, data):
        self.update_values(data)

    def get(self):
        if self.is_ready():
            drift = self.n_day_drift(self.time_period_kelly)
            volatility = self.n_day_volatility(self.time_period_kelly) 
            return drift / (volatility ** 2)
        else:
            return None
