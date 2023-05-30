from serial.tools import list_ports
import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from time import time

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
ax=fig.add_subplot(1,1,1)
xs=[0]
ys=[50]

tzero= time()

def animate(i, xs, ys):
    data=ser.readline()
    print(data)
    temp=""
    if data:
        temp = str(data)
        temp = temp[2:4]
    print(temp)
    
    tnow = time() - tzero
    
    xs.append(tnow)
    ys.append(temp)
    
    ax.clear()
    ax.plot(xs, ys)
    
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('Temperature vs Time')
    plt.ylabel('Temperature')
    plt.xlabel('Time')
ani = animation.FuncAnimation(fig, animate, fargs=(xs,ys), interval=2000)
plt.show()