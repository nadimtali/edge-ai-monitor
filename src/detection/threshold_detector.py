class ThresholdDetector:
    def __init__(self):
        self.thresholds = {}

    def add_threshold(self, sensor_name, warning_limit, critical_limit):
        self.thresholds[sensor_name] = {
            "warning": warning_limit,
            "critical": critical_limit,
        }

    def check(self, sensor_name, value):
        limits = self.thresholds.get(sensor_name)

        if limits is None:
            return "UNKNOWN"

        if value >= limits["critical"]:
            return "CRITICAL"

        if value >= limits["warning"]:
            return "WARNING"

        return "OK"