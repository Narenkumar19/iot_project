import os,time,numpy as np,pandas as pd,psutil,platform
import plotly.graph_objects as go
from IPython.display import clear_output,display
from datetime import datetime
history=[]
def collect():
    cpu=psutil.cpu_percent(interval=.5); ram=psutil.virtual_memory().percent
    disk=psutil.disk_usage(os.path.abspath(os.sep)).percent
    try:
        temps=psutil.sensors_temperatures(); temp=next((e.current for es in temps.values() for e in es if e.current is not None),np.nan)
    except: temp=np.nan
    try:
        bat=psutil.sensors_battery(); battery=np.nan if bat is None else bat.percent
    except: battery=np.nan
    return {"Time":datetime.now(),"CPU":cpu,"RAM":ram,"Disk":disk,"Temperature":temp,"Battery":battery}
def score(d):
    s=100
    s-=25 if d["CPU"]>90 else 10 if d["CPU"]>75 else 0
    s-=20 if d["RAM"]>90 else 10 if d["RAM"]>75 else 0
    s-=20 if d["Disk"]>95 else 10 if d["Disk"]>85 else 0
    if not np.isnan(d["Temperature"]): s-=30 if d["Temperature"]>85 else 15 if d["Temperature"]>70 else 0
    if not np.isnan(d["Battery"]): s-=20 if d["Battery"]<10 else 10 if d["Battery"]<20 else 0
    return max(0,min(100,s))
def dashboard():
    global history
    d=collect(); history.append(d); history=history[-40:]; df=pd.DataFrame(history); sc=score(d)
    status="NORMAL" if sc>=80 else "WARNING" if sc>=60 else "CRITICAL"
    clear_output(wait=True); print("SMART DEVICE HEALTH IoT MONITOR\n"+"="*55)
    for k in ["CPU","RAM","Disk","Temperature","Battery"]:
        v=d[k]; print(f"{k:14}: N/A" if np.isnan(v) else f"{k:14}: {v:.2f}")
    print(f"Health Score   : {sc:.1f}/100"); print(f"Status         : {status}")
    fig=go.Figure()
    for c in ["CPU","RAM","Disk","Temperature","Battery"]: fig.add_trace(go.Scatter(x=df.Time,y=df[c],mode="lines",name=c))
    fig.update_layout(title="Device Health History",height=550); display(fig)
    df.to_csv("device_health_data.csv",index=False)
dashboard()
