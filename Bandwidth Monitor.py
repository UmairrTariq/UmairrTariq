# Real-Time Bandwidth Monitor in Python

import time
import psutil
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

timestamps = []
mb_rec = []
mb_sent = []

last_rec = psutil.net_io_counters().bytes_recv
last_sent = psutil.net_io_counters().bytes_sent

def update_data(i):
    global last_rec,last_sent
    bytes_rec = psutil.net_io_counters().bytes_recv
    bytes_sent = psutil.net_io_counters().bytes_sent
    
    new_rec = (bytes_rec-last_rec)/1024/1024
    new_sent = (bytes_sent-last_sent)/1024/1024
    
    timestamps.append(time.time())
    mb_rec.append(new_rec)
    mb_sent.append(new_sent)
    
    if len(timestamps) > 600:
        timestamps.pop(0)
        mb_rec.pop(0)
        mb_sent.pop(0)
        
    ax.clear()
    ax.plot(timestamps,mb_rec,label = 'MB Received')
    ax.plot(timestamps,mb_sent,label = 'MB Sent')
    
    ax.legend()
    
    last_rec = bytes_rec
    last_sent = bytes_sent

# Intializ the plot
fig,ax = plt.subplots()
plt.xlabel('Time')
plt.ylabel('MB')
plt.title("Real-Time Bandwidth utilization")

ani = FuncAnimation(fig,update_data,interval = 1000)
plt.show()