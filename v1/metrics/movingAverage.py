import requests

class MovingAverage():
    def __init__(self, size, ticker, API_KEY):
        self.size = size
        self.values = []

    def update(self, data):
        self.add(data['close'])

    def get(self):
        return sum(self.values) / len(self.values)

    def add(self, value):
        self.values.append(value)

        if len(self.values) > self.size:
            self.values.pop(0)

    def reset(self):
        self.values = []

    def __str__(self):
        return str(self.get())

    def __repr__(self):
        return str(self.get())


