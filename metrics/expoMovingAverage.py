class ExpoMovingAverage():
    def __init__(self, size, smoothing=2):
        self.size = size
        self.values = []
        self.prev = 0
        self.smoothing = smoothing
        self.curr_value = 0

    def update(self, data):
        if len(self.values) >= self.size:
            data['close'] * (self.smoothing / (1 + self.size))
        else:
            self.curr_value = data['close']
            self.add(data['close'])
            if len(self.values) == self.size:
                self.prev = sum(self.values) / self.size

    def get(self):
        if len(self.values) >= self.size:

        else:
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


