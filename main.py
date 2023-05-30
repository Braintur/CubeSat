import serial
from serial.tools import list_ports
from time import sleep

strLine = None

ports = list_ports.comports()
numports = len(ports)

for i in range(0, numports):
    port = str(ports[i])
    print(port)
    #if "Arduino" in port:
        #   ser = serial.Serial(port[0:5], 9600, timeout=1)
    if "COM17" in port:
        ser = serial.Serial(port[0:5], 9600, timeout=1)


def get_from_serial(): #func that working in multiprocessing and catching data from serial port
    while True:
        for i in range(50):
            line = ser.readline()
            if line:
                line=line.decode()
                print(line)
                print(type(line))
                
        sleep(1)

def decode_from_radio(data): #not in use now
    if len(data)!=2:
        converted=""
        for i in data:
            if i!="\r\n":
                converted = converted+chr(int(i, 16))
        print(converted)
    return converted
                
get_from_serial() #init func