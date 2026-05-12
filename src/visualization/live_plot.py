import matplotlib.pyplot as plt
from collections import deque


class LivePlot:
    def __init__(self, max_points=50):
        self.max_points = max_points
        self.data = {}
        self.units = {}
        self.status = {}
        self.thresholds = {}

    def add_sensor(self, sensor_name, unit, warning_limit=None, critical_limit=None):
        self.data[sensor_name] = deque(maxlen=self.max_points)
        self.units[sensor_name] = unit
        self.status[sensor_name] = "OK"

        self.thresholds[sensor_name] = {
            "warning": warning_limit,
            "critical": critical_limit,
        }

    def update(self, sensor_name, value, status):
        self.data[sensor_name].append(value)
        self.status[sensor_name] = status

    def get_color(self, status):
        if status == "CRITICAL":
            return "red"
        if status == "WARNING":
            return "orange"
        return "green"

    def draw(self):
        plt.clf()

        number_of_sensors = len(self.data)

        for index, (sensor_name, values) in enumerate(self.data.items(), start=1):
            plt.subplot(number_of_sensors, 1, index)

            current_status = self.status[sensor_name]
            color = self.get_color(current_status)

            plt.plot(values, color=color)

            limits = self.thresholds[sensor_name]

            if limits["warning"] is not None:
                plt.axhline(
                    limits["warning"],
                    linestyle="--",
                    linewidth=1,
                    label="Warning limit"
                )

            if limits["critical"] is not None:
                plt.axhline(
                    limits["critical"],
                    linestyle=":",
                    linewidth=1,
                    label="Critical limit"
                )

            plt.title(f"{sensor_name} [{current_status}]")
            plt.ylabel(self.units[sensor_name])
            plt.grid(True)
            plt.legend(loc="upper right")

            if index == number_of_sensors:
                plt.xlabel("Time")

        plt.suptitle("Edge AI Monitoring System")
        plt.tight_layout()
        plt.pause(0.01)