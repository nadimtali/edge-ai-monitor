import csv
from datetime import datetime


class SensorLogger:

    def __init__(self, filename):

        self.filename = filename

        with open(self.filename, mode="w", newline="") as file:

            writer = csv.writer(file)

            writer.writerow([
                "Timestamp",
                "Sensor",
                "Raw Value",
                "Filtered Value",
                "Status"
            ])

    def log(self, sensor_name, raw_value, filtered_value, status):

        timestamp = datetime.now().strftime("%H:%M:%S")

        with open(self.filename, mode="a", newline="") as file:

            writer = csv.writer(file)

            writer.writerow([
                timestamp,
                sensor_name,
                raw_value,
                filtered_value,
                status
            ])