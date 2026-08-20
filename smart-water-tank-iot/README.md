# Smart Water Tank IoT Monitoring System

**Minor Project | Software-only IoT Project**

## Overview
A software-only IoT simulation for monitoring water level, inlet flow, outlet flow, estimated usage and tank status through an interactive dashboard.

## Monitored Parameters
- Water Level
- Inlet Flow
- Outlet Flow
- Estimated Usage
- Tank Status

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
Open `notebooks/smart-water-tank-iot.ipynb` in Google Colab and run the cells.

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
- Ultrasonic sensor integration
- MQTT
- Cloud database
- Automatic pump control

## Author
Naren Kumar, M.Tech, SRM University
