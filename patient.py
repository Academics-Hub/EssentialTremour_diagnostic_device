import portListener
import arduino
import tkinter
import customtkinter
import pandas 
import threading
import time

class Patient:
    def __init__(self):
        self.name: str = "no name brand"
        self.time: int = 0
        self.data: pandas.DataFrame = pandas.DataFrame()
        self.status: str = "unfinished"
        
    def __countdown(self, label: tkinter.Label, root: customtkinter.CTk):
        count = self.time
        for i in range(count+1):
            label.config(text=str(i))
            time.sleep(1)
        root.destroy()
            
    def __record(self):
        p = portListener.portListener()
        port = p.findArduino()
        a = arduino.Arduino(port, 9600)
        csv = self.name + "-" + str(self.time) + ".csv"
        a.read(csv, self.time)
        self.data = pandas.read_csv(csv)

    def __returnPatient(self, timeEntry: customtkinter.CTkEntry, nameEntry: customtkinter.CTkEntry, root: customtkinter.CTk):
        self.time = int(timeEntry.get())
        self.name = str(nameEntry.get())
        root.destroy()
        self.__recordingTimer()
        
    def __recordingTimer(self):
        root = customtkinter.CTk()
        root.title("Recording Patient Data")
        timerLabel = tkinter.Label(root, text="0", fg="white", bg="#2A2A2A")
        timerLabel.justify = tkinter.CENTER
        timerLabel.config(font=("Courier", 55, "bold"))
        timerLabel.config(width=4)
        timerLabel.config(height=2)
        timerLabel.pack()
        countdown_thread = threading.Thread(target=self.__countdown, args=(timerLabel, root))
        recording_thread = threading.Thread(target=self.__record, args=())
        recording_thread.start()
        countdown_thread.start()
        root.mainloop()
        countdown_thread.join()
        recording_thread.join()
    
    def recordPatient(self):
        root = customtkinter.CTk()
        root.title("Recording Time")
        root.geometry = ("120x220")
        query = customtkinter.CTkLabel(root, text="Patient name and how long would you like to record data for (seconds)")
        query.pack()
        nameEntry = customtkinter.CTkEntry(root)
        nameEntry.pack()
        timeEntry = customtkinter.CTkEntry(root)
        timeEntry.pack()
        confirmButton = customtkinter.CTkButton(root, text="Confirm", command=lambda: self.__returnPatient(timeEntry, nameEntry, root))
        confirmButton.pack(side=tkinter.BOTTOM)
        
    
    def getData(self):
        return self.data
    
    def getTime(self):
        return self.time
    
    def getName(self):
        return self.name
    
 
    
       