from collections import deque
import statistics


class StatisticalDetector:
    def __init__(self, window_size=20, z_threshold=2.5):
        self.window_size = window_size
        self.z_threshold = z_threshold
        self.history = {}

    def add_sensor(self, sensor_name):
        self.history[sensor_name] = deque(maxlen=self.window_size)

    def check(self, sensor_name, value):
        if sensor_name not in self.history:
            self.add_sensor(sensor_name)

        values = self.history[sensor_name]

        if len(values) < 5:
            values.append(value)
            return "OK", 0.0

        mean = statistics.mean(values)
        std = statistics.stdev(values)

        if std == 0:
            z_score = 0.0
        else:
            z_score = abs((value - mean) / std)

        values.append(value)

        if z_score >= self.z_threshold:
            return "ANOMALY", z_score

        return "OK", z_score