import serial
from datetime import datetime
import csv
import tkinter
class Arduino:
    def __init__(self, port, baudrate):
        self.port = port
        self.baudrate = baudrate
    
    def read(self, filename, timer):
        ser = serial.Serial(self.port, self.baudrate)
        self.timer = timer
        t1 = datetime.now()
        data = []
        with open(filename, 'w') as f:
            writer = csv.writer(f)
            while True:
                if (datetime.now() - t1).seconds > timer:
                    break
                temp = ser.readline().decode().strip()
                temp = int(temp)
                data.append(int(temp))
            for i in range(len(data)):
                writer.writerow([data[i]])
        ser.close()
    
