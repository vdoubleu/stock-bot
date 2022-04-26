from metrics.movingAverage import MovingAverage
from metrics.expoMovingAverage import ExpoMovingAverage
from metrics.RSI import RSI
from metrics.kellyCrit import KellyCrit

def init_metrics(ticker, API_KEY):
    return {
        # 'moving_average_5': MovingAverage(5, ticker, API_KEY),
        # 'expo_moving_average_5': ExpoMovingAverage(5, ticker, API_KEY),
        'rsi': RSI(5, ticker, API_KEY),
        'kelly_crit': KellyCrit(5, 5)
    }

def update_metrics(metrics, data):
    for metric in metrics:
        metrics[metric].update(data)

def get_metrics(metrics):
    return {
        metric: metrics[metric].get()
        for metric in metrics
    }

