import tkinter
import pandas
import signalProcessing

class Analysis:
    def __init__(self, canvas: tkinter.Canvas, data: pandas.DataFrame):
        self.canvas = canvas
        self.time_signal = data
        self.frequency_signal = signalProcessing.signal(data).applyFourierTransform()