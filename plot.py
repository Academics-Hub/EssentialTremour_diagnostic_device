import tkinter
import matplotlib.pyplot
import matplotlib.backends.backend_tkagg
import signalProcessing
import pandas
import numpy

class Plot: 
    def __init__(self, canvas: tkinter.Canvas, data: pandas.DataFrame, time:int):
        self.canvas = canvas
        self.time = time
        self.timeFigure = matplotlib.pyplot.Figure(figsize=(5,5), dpi=100)
        self.frequencyFigure = matplotlib.pyplot.Figure(figsize=(5,5), dpi=100)
        self.signal = signalProcessing.signal(data)
        self.data = data
       
    def __originalSignal(self):
        originalPlot = self.timeFigure.add_subplot(1, 1, 1)
        originalPlot.set_title('Recorded change in acceleration')
        originalPlot.set_xlabel('time (' + str(self.time) + 's)')
        originalPlot.set_ylabel('Amplitude (m/s^2)')
        originalPlot.set_xticks([])
        originalPlot.plot(numpy.arange(len(self.signal.data.iloc[:, 0])), self.signal.data.iloc[:, 0])
    
    def __transformedSignal(self):
        transformedPlot = self.frequencyFigure.add_subplot(1, 1, 1)
        transformedPlot.set_title('Frequency analysis')
        transformedPlot.psd(self.data, Fs=1000, antialiased=True)
        
    def createPatientPlot(self):
        self.__originalSignal()
        self.__transformedSignal()
        timePlot = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(self.timeFigure, self.canvas)
        timePlot.get_tk_widget().place(relx=0.3, rely=0.5, anchor=tkinter.CENTER, relwidth=0.5, relheight=0.9)
        frequencyPlot = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(self.frequencyFigure, self.canvas)
        frequencyPlot.get_tk_widget().place(relx=0.7, rely=0.5, anchor=tkinter.CENTER, relwidth=0.5, relheight=0.9)
        