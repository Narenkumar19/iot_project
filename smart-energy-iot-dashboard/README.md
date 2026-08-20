# Smart Energy IoT Monitoring Dashboard

**Major Project | Software-only IoT Project**

## Overview
A simple software-only IoT energy monitoring system that simulates voltage, current, power, energy consumption and estimated cost with a dashboard and alerts.

## Monitored Parameters
- Voltage
- Current
- Power
- Energy
- Estimated Cost

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
Open `notebooks/smart-energy-iot-dashboard.ipynb` in Google Colab and run the cells.

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
- Smart meter integration
- MQTT
- Cloud analytics
- Energy forecasting

## Author
Naren Kumar, M.Tech, SRM University
