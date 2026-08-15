"""
Smart IoT Device Battery Management System
===========================================

Software-only device health and battery monitoring agent.

Run locally on the target computer:
    python src/device_bms.py

The script displays a terminal dashboard and can optionally save
collected telemetry to CSV.
"""

import os
import platform
import socket
import time
from datetime import datetime

import numpy as np
import pandas as pd
import psutil


MAX_HISTORY = 100


def get_temperature():
    """Return a representative system temperature in Celsius when available."""
    try:
        temperatures = psutil.sensors_temperatures(fahrenheit=False)
        if not temperatures:
            return np.nan

        preferred = ("coretemp", "k10temp", "cpu_thermal", "cpu-thermal")
        for name in preferred:
            if name in temperatures:
                for entry in temperatures[name]:
                    if entry.current is not None:
                        return float(entry.current)

        for entries in temperatures.values():
            for entry in entries:
                if entry.current is not None:
                    return float(entry.current)
    except (AttributeError, OSError, PermissionError):
        pass

    return np.nan


def get_battery():
    """Return battery percentage and plugged-in state."""
    try:
        battery = psutil.sensors_battery()
        if battery is None:
            return np.nan, None
        return float(battery.percent), bool(battery.power_plugged)
    except (AttributeError, OSError, PermissionError):
        return np.nan, None


def get_device_data():
    """Collect one telemetry sample from the current operating system."""
    cpu = psutil.cpu_percent(interval=0.5)
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage(os.path.abspath(os.sep)).percent

    temperature = get_temperature()
    battery, plugged = get_battery()

    net = psutil.net_io_counters()
    uptime_hours = (time.time() - psutil.boot_time()) / 3600

    return {
        "Time": datetime.now().isoformat(timespec="seconds"),
        "CPU": round(cpu, 2),
        "RAM": round(ram, 2),
        "Disk": round(disk, 2),
        "Temperature": None if np.isnan(temperature) else round(temperature, 2),
        "Battery": None if np.isnan(battery) else round(battery, 2),
        "Plugged": plugged,
        "Sent_MB": round(net.bytes_sent / (1024 ** 2), 2),
        "Received_MB": round(net.bytes_recv / (1024 ** 2), 2),
        "Uptime_hours": round(uptime_hours, 2),
    }


def calculate_health(data):
    """Calculate a transparent rule-based device health score."""
    score = 100.0

    if data["CPU"] > 90:
        score -= 25
    elif data["CPU"] > 75:
        score -= 10

    if data["RAM"] > 90:
        score -= 20
    elif data["RAM"] > 75:
        score -= 10

    if data["Disk"] > 95:
        score -= 20
    elif data["Disk"] > 85:
        score -= 10

    if data["Temperature"] is not None:
        if data["Temperature"] > 85:
            score -= 30
        elif data["Temperature"] > 70:
            score -= 15

    if data["Battery"] is not None:
        if data["Battery"] < 10:
            score -= 20
        elif data["Battery"] < 20:
            score -= 10

    score = max(0.0, min(100.0, score))

    if score >= 80:
        status = "NORMAL"
    elif score >= 60:
        status = "WARNING"
    else:
        status = "CRITICAL"

    return round(score, 1), status


def generate_alerts(data):
    """Return active threshold alerts."""
    alerts = []

    if data["CPU"] > 90:
        alerts.append("HIGH CPU USAGE")
    elif data["CPU"] > 75:
        alerts.append("ELEVATED CPU USAGE")

    if data["RAM"] > 90:
        alerts.append("HIGH RAM USAGE")
    elif data["RAM"] > 75:
        alerts.append("ELEVATED RAM USAGE")

    if data["Disk"] > 95:
        alerts.append("DISK ALMOST FULL")
    elif data["Disk"] > 85:
        alerts.append("HIGH DISK USAGE")

    if data["Temperature"] is not None:
        if data["Temperature"] > 85:
            alerts.append("CRITICAL TEMPERATURE")
        elif data["Temperature"] > 70:
            alerts.append("HIGH TEMPERATURE")

    if data["Battery"] is not None:
        if data["Battery"] < 10:
            alerts.append("CRITICAL BATTERY")
        elif data["Battery"] < 20:
            alerts.append("LOW BATTERY")

    return alerts


def print_dashboard(data, score, status, alerts):
    """Print a compact terminal dashboard."""
    os.system("cls" if os.name == "nt" else "clear")

    print("=" * 72)
    print("        SMART IoT DEVICE BATTERY MANAGEMENT SYSTEM")
    print("                 DEVICE HEALTH MONITOR")
    print("=" * 72)

    print(f"Device       : {socket.gethostname()}")
    print(f"OS           : {platform.system()} {platform.release()}")
    print(f"Time         : {data['Time']}")
    print("-" * 72)

    print(f"CPU Usage    : {data['CPU']:>7.2f} %")
    print(f"RAM Usage    : {data['RAM']:>7.2f} %")
    print(f"Disk Usage   : {data['Disk']:>7.2f} %")

    temp = "N/A" if data["Temperature"] is None else f"{data['Temperature']:.2f} °C"
    battery = "N/A" if data["Battery"] is None else f"{data['Battery']:.2f} %"

    print(f"Temperature  : {temp:>12}")
    print(f"Battery      : {battery:>12}")

    power = "N/A"
    if data["Plugged"] is not None:
        power = "PLUGGED IN" if data["Plugged"] else "ON BATTERY"
    print(f"Power State  : {power:>12}")

    print(f"Uptime       : {data['Uptime_hours']:>7.2f} h")
    print("-" * 72)

    print(f"HEALTH SCORE : {score:>7.1f} / 100")
    print(f"STATUS       : {status}")

    print("-" * 72)
    print("ALERTS")

    if alerts:
        for alert in alerts:
            print(f"  [!] {alert}")
    else:
        print("  [OK] No abnormal conditions detected")

    print("=" * 72)


def run_monitor(interval=5, csv_path="data/device_telemetry.csv"):
    """Continuously monitor the device and save telemetry to CSV."""
    history = []

    print("Starting Smart IoT Device BMS...")
    print("Press Ctrl+C to stop.\n")

    try:
        while True:
            data = get_device_data()
            score, status = calculate_health(data)
            alerts = generate_alerts(data)

            data["Health_Score"] = score
            data["Status"] = status
            data["Alerts"] = " | ".join(alerts)

            history.append(data)
            history = history[-MAX_HISTORY:]

            os.makedirs(os.path.dirname(csv_path) or ".", exist_ok=True)
            pd.DataFrame(history).to_csv(csv_path, index=False)

            print_dashboard(data, score, status, alerts)
            print(f"\nTelemetry saved to: {csv_path}")
            time.sleep(interval)

    except KeyboardInterrupt:
        print("\nMonitoring stopped safely.")


if __name__ == "__main__":
    run_monitor()
