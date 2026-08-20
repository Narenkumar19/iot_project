# Smart Room IoT Monitoring System

**Minor Project | Software-only IoT Project**

## Overview
A simple software-only IoT simulation that monitors room temperature, humidity, light level, occupancy and room status through an interactive dashboard.

## Monitored Parameters
- Temperature
- Humidity
- Light Level
- Occupancy
- Room Status

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
Open `notebooks/smart-room-iot-monitor.ipynb` in Google Colab and run the cells.

## Local Run
```bash
pip install -r requirements.txt
python src/main.py
```

## Technologies
- Python
- Pandas
- NumPy
- Plotly
- Google Colab

## Future Scope
- MQTT communication
- ESP32 sensor integration
- Cloud storage
- Mobile alerts

## Author
Naren Kumar, M.Tech, SRM University
