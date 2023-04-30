import portListener
import arduino
import tkinter
import pandas 
import threading
import time

class patient:
    def __init__(self, name: str):
        self.name = name
        
    def __countdown(self, count: int, label: tkinter.Label, root: tkinter.Tk):
        for i in range(count+1):
            label.config(text=str(i))
            time.sleep(1)
        root.destroy()
            
    def __record(self, time: int):
        timer = time
        global data
        p = portListener.portListener()
        port = p.findArduino()
        a = arduino.Arduino(port, 9600)
        csv = self.name + ".csv"
        a.read(csv, timer)
        data = pandas.read_csv(csv)
        tkinter.messagebox.showinfo("Success", "Patient data read successfully")
        
    def __time(self, entry: tkinter.Entry) -> int:
        time = int(entry.get())
        return time
    
    def __returnTime(self, entry: tkinter.Entry, root: tkinter.Tk):
        global timer
        timer = self.__time(entry)
        root.destroy()
        self.__recordingTimer()
        
    def __recordingTimer(self):
        root = tkinter.tkinter()
        root.title("Recording Patient Data")
        root.geometry = ("100x100")
        timerLabel = tkinter.Label(root, text="0")
        timerLabel.justify = tkinter.CENTER
        timerLabel.config(font=("Courier", 55))
        timerLabel.config(width=8)
        timerLabel.config(height=4)
        timerLabel.pack()
        countdown_thread = threading.Thread(target=self.__countdown, args=(timer, timerLabel, root))
        recording_thread = threading.Thread(target=self.__record, args=(timer,))
        
        countdown_thread.start()
        recording_thread.start()
        
        root.mainloop()
        countdown_thread.join()
        #recording_thread.join()
    
    def recordPatient(self):
        root = tkinter.tkinter()
        root.title("Recording Time")
        root.geometry = ("100x200")
        query = tkinter.Label(root, text="How long would you like to record data for (seconds)?")
        query.pack()
        entry = tkinter.Entry(root)
        entry.pack()
        confirmButton = tkinter.Button(root, text="Confirm", command=lambda: self.__returnTime(entry, root))
        confirmButton.pack(side=tkinter.BOTTOM)
    
       