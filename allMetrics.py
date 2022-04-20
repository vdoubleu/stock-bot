from metrics.movingAverage import MovingAverage

def init_metrics(ticker, API_KEY):
    return {
        'moving_average_5': MovingAverage(5, ticker, API_KEY),
        'moving_average_10': MovingAverage(10, ticker, API_KEY),
        'moving_average_20': MovingAverage(20, ticker, API_KEY),
        'moving_average_50': MovingAverage(50, ticker, API_KEY),
        'moving_average_100': MovingAverage(100, ticker, API_KEY),
        'moving_average_200': MovingAverage(200, ticker, API_KEY),
    }

def update_metrics(metrics, data):
    for metric in metrics:
        metrics[metric].update(data)

def get_metrics(metrics):
    return {
        metric: metrics[metric].get()
        for metric in metrics
    }

