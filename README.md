# Edge AI Monitor

Real-time embedded monitoring and anomaly detection prototype built with Python.

## Overview

This project simulates an edge AI monitoring system that continuously tracks sensor data in real time and detects abnormal operating conditions using lightweight processing algorithms.

The system monitors:
- Motor temperature
- Vibration levels
- RPM (rotational speed)

The platform includes:
- Real-time live plotting
- Threshold-based anomaly detection
- Moving average filtering
- Sensor event logging
- CSV telemetry recording
- Modular software architecture

## Technologies Used

- Python
- Matplotlib
- NumPy
- CSV logging
- Object-oriented programming

## System Architecture

edge-ai-monitor/
│
├── src/
│   ├── detection/
│   ├── sensors/
│   ├── utils/
│   └── visualization/
│
├── logs/
├── main.py
├── config.py
└── requirements.txt

Author

Nadim Tali
Electrical Engineering Student – Microelectronics Specialization

```text
Sensors → Signal Processing → Fault Detection → Event Logger → Live Visualization
```bash
pip install -r requirements.txt
python main.py
