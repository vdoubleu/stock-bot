import math
from collections import deque

class GeoBrownian():
    def __init__(self, time_period):
        self.log_diff_prices = deque(maxlen=time_period)
        self.values = deque(maxlen=time_period + 1)
        self.time_period = time_period

    def update_values(self, data):
        self.values.append(data['close'])
        if len(self.values) > 1:
            self.log_diff_prices.append(math.log(self.values[-1] / self.values[-2]))

    def is_ready(self):
        return len(self.log_diff_prices) > 1

    def get_drift(self):
        if len(self.log_diff_prices) > 0:
            return sum(self.log_diff_prices) / self.time_period        
        else:
            return None

    def get_variance(self):
        drift = self.get_drift()

        return sum([(x - drift) ** 2 for x in self.log_diff_prices]) / (self.time_period - 1)

    def get_estimator(self):
        return self.get_drift() + (self.get_variance() / 2)

    def n_day_drift(self, n):
        return self.get_estimator() * n

    def n_day_volatility(self, n):
        return math.sqrt(self.get_variance() * n)
