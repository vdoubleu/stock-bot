from metrics.movingAverage import MovingAverage

def init_metrics(ticker, API_KEY):
    return {
        'moving_average_5': MovingAverage(5, ticker, API_KEY),
    }

def update_metrics(metrics, data):
    for metric in metrics:
        metrics[metric].update(data)

def get_metrics(metrics):
    return {
        metric: metrics[metric].get()
        for metric in metrics
    }

