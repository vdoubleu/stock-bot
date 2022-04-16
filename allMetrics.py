from metrics.movingAverage import MovingAverage

def init_metrics():
    return {
        'moving_average_5': MovingAverage(5),
        'moving_average_10': MovingAverage(10),
        'moving_average_20': MovingAverage(20),
        'moving_average_50': MovingAverage(50),
        'moving_average_100': MovingAverage(100),
        'moving_average_200': MovingAverage(200),
    }

def update_metrics(metrics, data):
    for metric in metrics:
        metrics[metric].update(data)

def get_metrics(metrics):
    return {
        metric: metrics[metric].get()
        for metric in metrics
    }

