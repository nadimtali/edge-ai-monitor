from src.sensors.sensor import SimulatedSensor
from src.visualization.live_plot import LivePlot

import time
import matplotlib.pyplot as plt
from src.utils.logger import SensorLogger
from src.detection.threshold_detector import ThresholdDetector
from src.utils.event_logger import EventLogger
from src.utils.signal_processor import MovingAverageFilter
from config import SENSOR_CONFIGS
from src.detection.statistical_detector import StatisticalDetector
from src.utils.system_report import SystemReporter
from src.utils.snapshot_manager import SnapshotManager

sensors = [
    SimulatedSensor(
        config["name"],
        config["unit"],
        config["start_value"],
        config["min_value"],
        config["max_value"],
        config["noise_range"],
        config["anomaly_chance"],
        config["anomaly_magnitude"],
    )
    for config in SENSOR_CONFIGS
]

plotter = LivePlot()
logger = SensorLogger("logs/sensor_data.csv")
event_logger = EventLogger("logs/events.csv")
detector = ThresholdDetector()
stat_detector = StatisticalDetector()

for config in SENSOR_CONFIGS:
    detector.add_threshold(
        config["name"],
        warning_limit=config["warning_limit"],
        critical_limit=config["critical_limit"],
    )

    plotter.add_sensor(
        config["name"],
        config["unit"],
        warning_limit=config["warning_limit"],
        critical_limit=config["critical_limit"],
    )

plotter.add_sensor("Motor Temperature", "°C", warning_limit=70, critical_limit=90)
plotter.add_sensor("Vibration", "mm/s", warning_limit=6, critical_limit=10)
plotter.add_sensor("RPM", "rpm", warning_limit=2200, critical_limit=2600)
plt.ion()

filter_system = MovingAverageFilter(window_size=5)

while True:
    readings = []

    for sensor in sensors:

        filter_system.add_sensor(sensor.name)

        raw_value, _ = sensor.read_value()
        
        value = round(filter_system.update(sensor.name, raw_value), 2)
        
        status = detector.check(sensor.name, value)
        ai_status, score = stat_detector.check(sensor.name, value)
        

        if ai_status == "ANOMALY":
            SnapshotManager.save_snapshot(sensor.name, "AI_ALERT")
            print(f"[AI DETECTOR] {sensor.name} anomaly detected | z-score={score:.2f}")
            
            if status == "OK":
                status = "AI ALERT"

        plotter.update(sensor.name, value, status)
        logger.log(sensor.name, raw_value, value, status)
        event_logger.log_event(sensor.name, value, status)
        

        readings.append({
            "name": sensor.name,
            "value": value,
            "unit": sensor.unit,
            "status": status,
            "ai_score": round(score, 2),
        })

    if status == "ANOMALY":
        print(f"[AI DETECTOR] {sensor.name} anomaly detected | z-score={score:.2f}")

    statuses = [reading["status"] for reading in readings]

    if "CRITICAL" in statuses:
        system_status = "CRITICAL"
    elif "WARNING" in statuses:
        system_status = "WARNING"
    else:
        system_status = "OK"

    ok_count = statuses.count("OK")
    warning_count = statuses.count("WARNING")
    critical_count = statuses.count("CRITICAL")
    
    SystemReporter.print_summary(readings, system_status)

    plotter.draw()

    time.sleep(1)