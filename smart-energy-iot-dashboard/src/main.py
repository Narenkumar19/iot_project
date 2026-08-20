import time,numpy as np,pandas as pd
import plotly.graph_objects as go
from IPython.display import clear_output,display
from datetime import datetime
history=[]; energy=0
def sensor_data():
    global energy
    v=np.random.normal(230,3); i=np.random.uniform(1,8); p=v*i/1000; energy+=p*(5/3600)
    return {"Time":datetime.now(),"Voltage":v,"Current":i,"Power":p,"Energy":energy,"Estimated Cost":energy*8}
def dashboard():
    global history
    d=sensor_data(); history.append(d); history=history[-40:]; df=pd.DataFrame(history)
    clear_output(wait=True); print("SMART ENERGY IoT MONITORING DASHBOARD\n"+"="*55)
    for k,v in d.items(): print(f"{k:18}: {v:.3f}" if isinstance(v,(float,np.floating)) else f"{k:18}: {v}")
    print("ALERT: High power consumption" if d["Power"]>1.5 else "Status: Normal")
    fig=go.Figure(go.Scatter(x=df.Time,y=df.Power,mode="lines+markers",name="Power"))
    fig.update_layout(title="Power Consumption History",yaxis_title="kW",height=500); display(fig)
    df.to_csv("energy_data.csv",index=False)
dashboard()
