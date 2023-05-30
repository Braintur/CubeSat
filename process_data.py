
def process_data_from_serial(data):
    from os import chdir
    from cv2 import VideoCapture, imwrite
    from random import randint
    from ops import bar_to_meters
    import matplotlib.pyplot as plt
    
    data = data.decode()
    print(data)
    
    #plt.ion()
    #fig = plt.figure()
    i=0 
    x=list()
    y=list()
    i=0

    if 't' in data:
        x.append(i)
        y.append(data)
        #plt.scatter(i, float(data))
        i+=1
        #plt.show()
        #plt.pause(0.0001)
        