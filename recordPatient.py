import portListener
import arduino
from tkinter import Label
from tkinter import messagebox
import pandas as pd
import tkinter as tk
import threading
import time

class patient:
    def __init__(self, name: str):
        self.name = name
        
    def __countdown(self, count: int, label: Label, root: tk.Tk):
        #edit the label widget to display the countdown
        for i in range(count+1):
            label.config(text=str(i))
            time.sleep(1)
        #destroy the root window
        root.destroy()
            
    def __record(self, time: int):
        #define timer
        timer = time
        #define data frame
        global df
        #define port listener object
        pl = portListener.portListener()
        #find port of arduino
        port = pl.findArduino()
        #define a new arduiuno at the port, with a baud rate of 9600
        a = arduino.arduino(port, 9600)
        #read data from the arduino for defined time
        #define csv file base off of patient name
        csv = self.name + ".csv"
        a.read(csv, timer)
        #move data into previously defined data frame
        df = pd.read_csv(csv)
        messagebox.showinfo("Success", "Patient data read successfully")
        
    def __time(self, entry: tk.Entry) -> int:
        time = int(entry.get())
        return time
    
    def __returnTime(self, entry: tk.Entry, root: tk.Tk):
        global timer
        timer = self.__time(entry)
        root.destroy()
        self.__record()
        
    def recordPatient(self):
        root = tk.Tk()
        root.title("Recording Time")
        root.geometry = ("100x200")
        query = Label(root, text="How long would you like to record data for (seconds)?")
        query.pack()
        
        entry = tk.Entry(root)
        entry.pack()
        
        confirmButton = tk.Button(root, text="Confirm", command=lambda: self.__returnTime(entry, root))
        confirmButton.pack(side=tk.BOTTOM)
        
    def __record(self):
        #define root window
        root = tk.Tk()
        root.title("Recording Patient Data")
        root.geometry = ("100x100")
        #define a label widget for the timer
        timerLabel = Label(root, text="0")
        timerLabel.justify = tk.CENTER
        timerLabel.config(font=("Courier", 55))
        timerLabel.config(width=8)
        timerLabel.config(height=4)
        timerLabel.pack()
        #defines multithreading for the countdown to run parrallel to the recording
        countdown_thread = threading.Thread(target=self.__countdown, args=(timer, timerLabel, root))
        recording_thread = threading.Thread(target=self.__record, args=(timer,))
        
        countdown_thread.start()
        recording_thread.start()
        
        root.mainloop()
        
        countdown_thread.join()
        recording_thread.join()
        
    
       