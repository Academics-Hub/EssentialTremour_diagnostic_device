import tkinter
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from signalProcessing import Signal

class Analysis:
    def __init__(self, canvas: tkinter.Canvas, data: pd.DataFrame, reference_signal: pd.DataFrame):
        self.canvas = canvas
        self.time_signal = data
        self.reference_signal = reference_signal
        self.frequency_signal = Signal(data).applyFourierTransform()
        self.reference_frequency_signal = Signal(reference_signal).applyFourierTransform()
        self.csd_patient = Signal.calculateCrossSpectralDensity(self.frequency_signal[1], self.reference_frequency_signal[1])
        self.csd_reference = Signal.calculateCrossSpectralDensity(self.reference_frequency_signal[1], self.reference_frequency_signal[1])

    def displayCSD(self):
        self.canvas.create_line(50, 50, 750, 50, width=2)
        self.canvas.create_line(50, 50, 50, 550, width=2)
        self.canvas.create_text(400, 30, text="Cross Spectral Density", font=("Arial", 20))

        x_scale = 700 / (self.csd_patient.shape[0] - 1)
        y_scale = 500 / (max(np.max(self.csd_patient), np.max(self.csd_reference)) - min(np.min(self.csd_patient), np.min(self.csd_reference)))

        # Plot patient's CSD
        for i in range(self.csd_patient.shape[0] - 1):
            x1 = 50 + i * x_scale
            y1 = 550 - (self.csd_patient[i] - min(np.min(self.csd_patient), np.min(self.csd_reference))) * y_scale
            x2 = 50 + (i + 1) * x_scale
            y2 = 550 - (self.csd_patient[i + 1] - min(np.min(self.csd_patient), np.min(self.csd_reference))) * y_scale
            self.canvas.create_line(x1, y1, x2, y2, width=2, fill="blue")

        # Plot reference CSD
        for i in range(self.csd_patient.shape[0] - 1):
            x1 = 50 + i * x_scale
            y1 = 550 - (self.csd_reference[i] - min(np.min(self.csd_patient), np.min(self.csd_reference))) * y_scale
            x2 = 50 + (i + 1) * x_scale
            y2 = 550 - (self.csd_reference[i + 1] - min(np.min(self.csd_patient), np.min(self.csd_reference))) * y_scale
            self.canvas.create_line(x1, y1, x2, y2, width=2, fill="red")

        self.canvas.pack()














