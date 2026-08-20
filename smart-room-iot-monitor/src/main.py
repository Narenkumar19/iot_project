import time, numpy as np, pandas as pd
import plotly.graph_objects as go
from IPython.display import clear_output, display
from datetime import datetime
history=[]
def sensor_data():
    t=np.random.normal(27,1.5); h=np.clip(np.random.normal(58,7),20,90)
    light=np.clip(np.random.normal(500,180),0,1000); occ=np.random.choice([0,1],p=[.35,.65])
    return {"Time":datetime.now(),"Temperature":t,"Humidity":h,"Light Level":light,
            "Occupancy":occ,"Room Status":"Occupied" if occ else "Empty"}
def dashboard():
    global history
    d=sensor_data(); history.append(d); history=history[-40:]; df=pd.DataFrame(history)
    clear_output(wait=True); print("SMART ROOM IoT MONITORING SYSTEM\n"+"="*55)
    for k,v in d.items():
        print(f"{k:14}: {v:.2f}" if isinstance(v,(float,np.floating)) else f"{k:14}: {v}")
    if d["Temperature"]>30: print("ALERT: High temperature")
    if d["Humidity"]>80: print("ALERT: High humidity")
    fig=go.Figure(); fig.add_trace(go.Scatter(x=df.Time,y=df["Temperature"],name="Temperature"))
    fig.add_trace(go.Scatter(x=df.Time,y=df["Humidity"],name="Humidity"))
    fig.update_layout(title="Room Sensor History",height=500); display(fig)
    df.to_csv("smart_room_data.csv",index=False)
dashboard()
