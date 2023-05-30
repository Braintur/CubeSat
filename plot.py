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
ax = fig.add_subplot(2,1,1)
bx = fig.add_subplot(2,1,2)
xs1=[0]*40
ys=list(range(40))
xs2=[0]*2000
zs=list(range(2000))

tzero = time()

def animate(i, xs, ys):
    data = ser.readline()
    data = data.decode()
    print(data)
    if len(data)>3:
        temp,lux = data[:-2].split(',')
        tnow = time()- tzero
        
        xs1.append(tnow)
        xs2.append(tnow)
        ys.append(temp)
        zs.append(lux)
        
        ax.clear()
        bx.clear()
        ax.plot(xs1, ys)
        bx.plot(xs2, zs)
        
        plt.xticks(rotation=45, ha='right')
        plt.subplots_adjust(bottom=0.30)
        plt.title("Temp over time")
        plt.ylabel('Temperature')
        plt.xlabel('Time')
        plt.yticks([0,200,400,600,800,100,1200,1400,1600,1800,2000])
    
ani = animation.FuncAnimation(fig, animate, fargs=(xs1, ys), interval=1000)
plt.show()