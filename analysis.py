import tkinter
import pandas
import signalProcessing

class Analysis:
    def __init__(self, canvas: tkinter.Canvas, data: pandas.DataFrame):
        self.canvas = canvas
        self.signal = signalProcessing.signal(data).applyFourierTransform()