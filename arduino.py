import serial
from datetime import datetime
import csv
import tkinter as tk
from tkinter import messagebox
import numpy as np
import time
class arduino:
    def __init__(self, port, baudrate):
        self.port = port
        self.baudrate = baudrate
    
    def read(self, filename, timer):
        ser = serial.Serial(self.port, self.baudrate)
        #print(t1)

        self.timer = timer
        messagebox.showinfo("Please wait", "Reading patient data for " + str(timer) + " seconds")

        t1 = datetime.now()
        data = []
        with open(filename, 'w') as f:
            writer = csv.writer(f)
            while True:
                if (datetime.now() - t1).seconds > timer:
                    break
                temp = ser.readline().decode().strip()
                data.append(int(temp))
            
            for i in range(len(data)):
                writer.writerow([data[i]])

        ser.close()
    
