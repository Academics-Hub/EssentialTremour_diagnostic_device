import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
import numpy as np
from signalProcessing import Signal

class Plot:
    def __init__(self, canvas: tk.Canvas, data: np.ndarray, time: int):
        self.canvas = canvas
        self.time = time
        self.timeFigure = plt.Figure(figsize=(5, 5), dpi=100)
        self.frequencyFigure = plt.Figure(figsize=(5, 5), dpi=100)
        self.signal = Signal(data)
        self.data = pd.DataFrame(data)  # Convert numpy array to pandas DataFrame

    def __originalSignal(self):
        originalPlot = self.timeFigure.add_subplot(1, 1, 1)
        #originalPlot.set_title('Recorded change in acceleration')
        originalPlot.set_xlabel('time (' + str(self.time) + 's)')
        originalPlot.set_ylabel('Amplitude (m/s^2)')
        originalPlot.set_xticks([])
        originalPlot.plot(np.arange(len(self.data.iloc[:, 0])), self.data.iloc[:, 0])

    def __transformedSignal(self):
        transformedPlot = self.frequencyFigure.add_subplot(1, 1, 1)
        transformedPlot.set_title('Frequency analysis')
        transformedPlot.psd(self.data, Fs=1000, antialiased=True)

    def createPatientPlot(self):
        self.__originalSignal()
        timePlot = FigureCanvasTkAgg(self.timeFigure, self.canvas)
        timePlot.get_tk_widget().place(relx=0, rely=0, relwidth=1, relheight=1)



        