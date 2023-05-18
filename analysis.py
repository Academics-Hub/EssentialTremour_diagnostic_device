import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np
import pandas

class Analysis:
    def __init__(self, canvas: tk.Canvas, data: pandas.DataFrame, reference_data: pandas.DataFrame):
        self.canvas = canvas
        self.time_signal = data
        self.reference_signal = reference_data

    def displayCSD(self):
        signal = self.time_signal.iloc[:, 0]
        reference_signal = self.reference_signal.iloc[:, 0]

        fs = 1000  # Set the sampling frequency
        f, csd = scipy.signal.csd(signal, reference_signal, fs=fs)

        # Clear the canvas
        self.canvas.delete("all")

        # Display the original signal
        self.canvas.create_text(400, 30, text="Original Signal", font=("Arial", 20))
        x_scale = 700 / (len(signal) - 1)
        y_scale = 500 / (np.max(signal) - np.min(signal))
        for i in range(len(signal) - 1):
            x1 = 50 + i * x_scale
            y1 = 550 - (signal[i] - np.min(signal)) * y_scale
            x2 = 50 + (i + 1) * x_scale
            y2 = 550 - (signal[i + 1] - np.min(signal)) * y_scale
            self.canvas.create_line(x1, y1, x2, y2, width=2, fill="blue")

        # Display the cross spectral density
        self.canvas.create_text(400, 580, text="Cross Spectral Density", font=("Arial", 20))
        fig = plt.Figure(figsize=(6, 4), dpi=100)
        ax = fig.add_subplot(111)
        ax.plot(f, np.abs(csd), color="red")
        ax.set_xlabel("Frequency (Hz)")
        ax.set_ylabel("Magnitude")
        canvas = FigureCanvasTkAgg(fig, master=self.canvas)
        canvas.draw()
        canvas.get_tk_widget().place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)




