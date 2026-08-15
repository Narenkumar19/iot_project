# Smart IoT Device Battery Management System

A software-based **IoT Device Battery and Health Management System** for monitoring the device on which the monitoring agent is running.

The system collects operating-system-level telemetry and presents it through an interactive dashboard. It can be used as a foundation for an M.Tech project in IoT, embedded systems, battery management, and intelligent device monitoring.

## Monitored Parameters

1. **CPU Usage (%)**
2. **RAM Usage (%)**
3. **Disk Usage (%)**
4. **CPU Temperature (°C)** — when exposed by the operating system
5. **Battery Level (%)** — when the device exposes battery information

Additional information:
- Plugged-in / battery power state
- System uptime
- Network traffic counters
- Device/OS information
- Device health score
- Automatic warning/critical alerts
- Historical plots

## System Architecture

```text
                DEVICE
                   |
       +-----------+-----------+
       |           |           |
      CPU         RAM       Battery/Power
       |           |           |
       +-----------+-----------+
                   |
            Python Monitoring
                 Agent
                   |
             BMS Analyzer
                   |
        +----------+----------+
        |                     |
  Health Score          Fault Detection
        |                     |
        +----------+----------+
                   |
          Interactive Dashboard
                   |
             Live Monitoring
```

## Project Features

- Real-time system monitoring
- Battery-aware device monitoring
- Rule-based health scoring
- Threshold-based fault detection
- Interactive Plotly dashboard
- Historical data visualization
- CSV export
- Works locally on Windows/Linux/macOS where supported by `psutil`

## Important: Google Colab vs. Your Actual Device

Google Colab runs your Python code on a remote virtual machine. Therefore:

- Running the notebook in **Colab monitors the Colab runtime**, not your physical laptop.
- To monitor your **actual laptop/PC**, run the Python agent locally on that device.
- For a true IoT implementation, the local agent can publish telemetry using MQTT/HTTP to a cloud dashboard.

## Quick Start — Google Colab

Open `notebooks/Smart_Device_BMS_Colab.ipynb` in Google Colab and run the cells.

Or upload `src/device_bms.py` to Colab and run:

```python
!pip install -r requirements.txt
```

Then import and use the monitoring functions.

## Quick Start — Local Computer

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/smart-iot-device-bms.git
cd smart-iot-device-bms
```

Create a virtual environment if desired:

```bash
python -m venv .venv
```

Activate it:

Windows:

```bash
.venv\Scripts\activate
```

Linux/macOS:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run:

```bash
python src/device_bms.py
```

## Health Score

The current prototype uses a transparent rule-based score:

- CPU > 75%: warning penalty
- CPU > 90%: critical penalty
- RAM > 75%: warning penalty
- RAM > 90%: critical penalty
- Disk > 85%: warning penalty
- Disk > 95%: critical penalty
- Temperature > 70°C: warning penalty
- Temperature > 85°C: critical penalty
- Battery < 20%: warning penalty
- Battery < 10%: critical penalty

The score is limited to 0–100.

### Status

| Score | Status |
|---:|---|
| 80–100 | NORMAL |
| 60–79 | WARNING |
| 0–59 | CRITICAL |

These thresholds are prototype values and should be calibrated for the target hardware.

## Suggested Future Research Extensions

- MQTT-based IoT telemetry
- Firebase/ThingsBoard integration
- ESP32 sensor integration
- Battery voltage/current sensors
- State-of-Charge estimation
- State-of-Health estimation
- Remaining Useful Life prediction
- Machine-learning anomaly detection
- Edge AI
- Predictive maintenance
- Cloud database storage
- Email/Telegram notification system

## Repository Structure

```text
smart-iot-device-bms/
├── notebooks/
│   └── Smart_Device_BMS_Colab.ipynb
├── src/
│   └── device_bms.py
├── data/
│   └── .gitkeep
├── screenshots/
│   └── .gitkeep
├── .gitignore
├── LICENSE
├── requirements.txt
└── README.md
```

## Technologies

- Python
- psutil
- Pandas
- NumPy
- Plotly
- Google Colab
- Jupyter Notebook

## Author

**Naren Kumar**

M.Tech Student  
SRM University

## Disclaimer

This is a software monitoring prototype. It is not a certified safety-critical battery management system. Hardware BMS protection functions such as cell balancing, over-current protection, short-circuit protection, and charge/discharge cutoff require appropriate hardware and validated safety circuitry.
