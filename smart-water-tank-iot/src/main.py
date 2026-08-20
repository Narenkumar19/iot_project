import time, numpy as np, pandas as pd
import plotly.graph_objects as go
from IPython.display import clear_output, display
from datetime import datetime
history=[]; level=72.0
def sensor_data():
    global level
    inlet=np.random.uniform(0,3); outlet=np.random.uniform(0,2.5); level=np.clip(level+inlet-outlet,0,100)
    status="LOW" if level<20 else "FULL" if level>90 else "NORMAL"
    return {"Time":datetime.now(),"Water Level":level,"Inlet Flow":inlet,"Outlet Flow":outlet,
            "Estimated Usage":outlet,"Tank Status":status}
def dashboard():
    global history
    d=sensor_data(); history.append(d); history=history[-40:]; df=pd.DataFrame(history)
    clear_output(wait=True); print("SMART WATER TANK IoT MONITORING SYSTEM\n"+"="*55)
    for k,v in d.items():
        print(f"{k:18}: {v:.2f}" if isinstance(v,(float,np.floating)) else f"{k:18}: {v}")
    if d["Water Level"]<20: print("ALERT: Refill required")
    fig=go.Figure(go.Scatter(x=df.Time,y=df["Water Level"],mode="lines+markers"))
    fig.update_layout(title="Water Level History",yaxis_title="Level (%)",height=500); display(fig)
    df.to_csv("water_tank_data.csv",index=False)
dashboard()
