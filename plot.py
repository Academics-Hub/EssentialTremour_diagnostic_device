import tkinter
import matplotlib.pyplot
import matplotlib.backends.backend_tkagg
import signalProcessing
import pandas
import numpy

class Plot:
    def __init__(self, canvas: tkinter.Canvas, data: pandas.DataFrame):
        self.canvas = canvas
        self.timeFigure = matplotlib.pyplot.Figure(figsize=(5,5), dpi=100)
        self.frequencyFigure = matplotlib.pyplot.Figure(figsize=(5,5), dpi=100)
        self.signal = signalProcessing.signal(data)
    
    def __time(self, entry: tkinter.Entry) -> int:
        time = int(entry.get())
        return time
    
    def __returnTime(self, entry: tkinter.Entry, root: tkinter.Tk):
        global timer
        timer = self.__time(entry)
        root.destroy()
        self.__draw()
       
    def __originalSignal(self):
        originalPlot = self.timeFigure.add_subplot(1, 1, 1)
        originalPlot.set_title('Recorded change in acceleration')
        originalPlot.set_xlabel('time (' + str(timer) + 's)')
        originalPlot.set_ylabel('Amplitude (m/s^2)')
        originalPlot.set_xticks([])
        originalPlot.plot(numpy.arange(len(self.signal.data.iloc[:, 0])), self.signal.data.iloc[:, 0])
    
    def __transformedSignal(self):
        frequencies, transformedSignal = self.signal.applyFourierTransform()
        transformedPlot = self.frequencyFigure.add_subplot(1, 1, 1)
        transformedPlot.set_title('Normalized frequency spectrum, \ndisplaying spikes in the \n90th percentile of frequencies')
        transformedPlot.set_xlabel('Frequency (Hz)')
        transformedPlot.set_yticks([])
        transformedPlot.plot(frequencies, transformedSignal)
        
    def __draw(self):
        self.__originalSignal()
        self.__transformedSignal()
        timePlot = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(self.timeFigure, self.canvas)
        timePlot.get_tk_widget().place(relx=0.3, rely=0.5, anchor=tkinter.CENTER, relwidth=0.5, relheight=0.6)
        frequencyPlot = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(self.frequencyFigure, self.canvas)
        frequencyPlot.get_tk_widget().place(relx=0.7, rely=0.5, anchor=tkinter.CENTER, relwidth=0.5, relheight=0.6)
        
    def createPatientPlot(self):
        root = tkinter.Tk()
        root.title("Plot Time")
        root.geometry = ("100x200")
        query = tkinter.Label(root, text="What timeframe would you like to plot for (seconds)?")
        query.pack()
        entry = tkinter.Entry(root)
        entry.pack()
        confirmButton = tkinter.Button(root, text="Confirm", command=lambda: self.__returnTime(entry, root))
        confirmButton.pack(side=tkinter.BOTTOM)
        