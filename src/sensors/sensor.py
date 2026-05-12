import random


class SimulatedSensor:
    def __init__(self, name, unit, start_value, min_value, max_value, noise_range, anomaly_chance, anomaly_magnitude):
        self.name = name
        self.unit = unit
        self.value = start_value
        self.min_value = min_value
        self.max_value = max_value
        self.noise_range = noise_range
        self.anomaly_chance = anomaly_chance
        self.anomaly_magnitude = anomaly_magnitude

    def read_value(self):
        normal_change = random.uniform(-self.noise_range, self.noise_range)
        self.value += normal_change

        is_anomaly = random.randint(1, 100) > self.anomaly_chance

        if is_anomaly:
            spike = random.uniform(*self.anomaly_magnitude)
            self.value += spike

        self.value = max(self.min_value, min(self.value, self.max_value))

        return round(self.value, 2), is_anomaly