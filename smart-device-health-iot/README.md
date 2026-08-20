# Smart Device Health IoT Monitor

**Major Project | Software-only IoT Project**

## Overview
A software-only IoT monitoring system that observes CPU, RAM, disk, temperature and battery status of a computing device and calculates a simple device health score.

## Monitored Parameters
- CPU Usage
- RAM Usage
- Disk Usage
- Temperature
- Battery Level

## Features
- Software IoT telemetry simulation
- Interactive Plotly dashboard
- Historical graphs
- CSV logging
- Simple threshold alerts
- Google Colab support

## Architecture
```text
Software Sensors / Device Data
            |
            v
      Python IoT Layer
            |
            v
       Data Processing
            |
            v
    Plotly Monitoring Dashboard
            |
            v
       Alerts + CSV Logs
```

## Google Colab
Open `notebooks/smart-device-health-iot.ipynb` in Google Colab and run the cells.

## Local Run
```bash
pip install -r requirements.txt
python src/main.py
```

## Technologies
- Python
- psutil
- Pandas
- Plotly
- Google Colab / Local Python

## Future Scope
- MQTT telemetry
- Cloud dashboard
- Anomaly detection
- Predictive maintenance

## Author
Naren Kumar, M.Tech, SRM University
