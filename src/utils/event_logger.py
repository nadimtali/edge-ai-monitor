import csv
from datetime import datetime


class EventLogger:
    def __init__(self, filename):
        self.filename = filename
        self.last_status = {}

        with open(self.filename, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Timestamp", "Sensor", "Value", "Previous Status", "New Status", "Message"])

    def log_event(self, sensor_name, value, status):
        previous_status = self.last_status.get(sensor_name, "OK")

        if status == previous_status:
            return

        self.last_status[sensor_name] = status

        timestamp = datetime.now().strftime("%H:%M:%S")

        if status == "OK":
            message = f"{sensor_name} recovered to OK"
        else:
            message = f"{sensor_name} changed from {previous_status} to {status}"

        with open(self.filename, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([timestamp, sensor_name, value, previous_status, status, message])