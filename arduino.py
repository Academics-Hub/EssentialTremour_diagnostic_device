import serial
import time
import csv
import math
import tkinter as tk
from tkinter import messagebox

def read(filename):
    #ser = serial.Serial('/dev/ttyACM0', 9600)
    time.sleep(1)

    timer = 10
    messagebox.showinfo("Please wait", "Reading patient data for " + str(timer) + " seconds")

    with open(filename, 'w') as f:
        writer = csv.writer(f)
        t = 0
        while timer >= 0:
            #data = ser.readline().decode().strip()
            data=2*math.sin(t)+2*math.cos(2*t)+2*math.sin(3*t)+2*math.cos(4*t)
            writer.writerow([t, data])
            timer -= 0.1
            t += 0.1
            time.sleep(0.1)
            print(timer)
    
