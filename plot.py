import serial
from serial.tools import list_ports
from time import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation

ports = list_ports.comports()
numports = len(ports)

for i in range(0, numports):
    port = str(ports[i])
    print(port)
    #if "Arduino" in port:
        #   ser = serial.Serial(port[0:5], 9600, timeout=1)
    if "COM17" in port:
        ser = serial.Serial(port[0:5], 9600, timeout=1)
        
    
fig = plt.figure()
ax = fig.add_subplot()
xs1=[0]*60
ys=list(range(60))
zs=list(range(60))

tzero = time()

def animate(i, xs, ys):
    data = ser.readline()
    data = data.decode()
    print(data)
    if len(data)>3:
        temp,lux = data[:-2].split(',')
        tnow = time()- tzero
        lux = int(lux)/1000
        xs1.append(tnow)
        ys.append(temp)
        zs.append(lux)
        
        ax.clear()
        plt.plot(xs, ys, label="Temperature (C)")
        plt.plot(xs, zs, label="Light (kilolux)")
        plt.legend()
        
        plt.xticks(rotation=45, ha='right')
        plt.yticks(range(0,60,10))
        
    
ani = animation.FuncAnimation(fig, animate, fargs=(xs1, ys))
plt.show()