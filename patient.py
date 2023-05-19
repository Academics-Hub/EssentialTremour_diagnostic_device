import portListener
import arduino
import tkinter
import pandas 
import threading
import time

class Patient:
    def __init__(self):
        self.name: str = "no name brand"
        self.time: int = 0
        self.data: pandas.DataFrame = pandas.DataFrame()
        
    def __countdown(self, label: tkinter.Label, root: tkinter.Tk):
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
        tkinter.messagebox.showinfo("Success", "Patient data read successfully")
    
    
    def __returnPatient(self, timeEntry: tkinter.Entry, nameEntry: tkinter.Entry, root: tkinter.Tk):
        self.time = int(timeEntry.get())
        self.name = str(nameEntry.get())
        root.destroy()
        self.__recordingTimer()
        
    def __recordingTimer(self):
        root = tkinter.Tk()
        root.title("Recording Patient Data")
        root.geometry = ("100x100")
        timerLabel = tkinter.Label(root, text="0")
        timerLabel.justify = tkinter.CENTER
        timerLabel.config(font=("Courier", 55))
        timerLabel.config(width=8)
        timerLabel.config(height=4)
        timerLabel.pack()
        countdown_thread = threading.Thread(target=self.__countdown, args=(timerLabel, root))
        recording_thread = threading.Thread(target=self.__record, args=())
        countdown_thread.start()
        recording_thread.start()
        root.mainloop()
        countdown_thread.join()
        recording_thread.join()
    
    def recordPatient(self):
        root = tkinter.Tk()
        root.title("Recording Time")
        root.geometry = ("100x200")
        query = tkinter.Label(root, text="Patient name and how long would you like to record data for (seconds)")
        query.pack()
        nameEntry = tkinter.Entry(root)
        nameEntry.pack()
        timeEntry = tkinter.Entry(root)
        timeEntry.pack()
        confirmButton = tkinter.Button(root, text="Confirm", command=lambda: self.__returnPatient(timeEntry, nameEntry, root))
        confirmButton.pack(side=tkinter.BOTTOM)
    
    def getData(self):
        return self.data
    
    def getTime(self):
        return self.time
    
       