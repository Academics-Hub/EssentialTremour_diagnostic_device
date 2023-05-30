import serial
import serial.tools.list_ports
from tkinter import messagebox

class portListener:
    def __init__(self):
        self.ports = list (serial.tools.list_ports.comports()) #creates list of available ports
        
    def findArduino(self): #returns port of arduino if found, else calls error function
        count = 0
        for p in self.ports:
            count += 1
        i = 0
        for p in self.ports:
            i += 1
            if "Nano 33 BLE" in p.description:
                return p.device
            elif i == count:
                return self.noArduino()
    
    def noArduino(self):
        messagebox.showerror("Error", "No Arduino Nano 33 BLE found. Please connect an Arduino Nano 33 BLE and try again.") #defines error message if arduino not plugged in