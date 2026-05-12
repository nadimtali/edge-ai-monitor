from collections import deque


class MovingAverageFilter:
    def __init__(self, window_size=5):
        self.window_size = window_size
        self.values = {}

    def add_sensor(self, sensor_name):
        self.values[sensor_name] = deque(maxlen=self.window_size)

    def update(self, sensor_name, value):
        self.values[sensor_name].append(value)

        return sum(self.values[sensor_name]) / len(self.values[sensor_name])