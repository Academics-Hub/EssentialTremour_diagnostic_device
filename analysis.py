import scipy.signal
import numpy as np
import matplotlib.pyplot as plt
import customtkinter
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

class Analysis:
    def __init__(self, analysis_canvas, patient_data, reference_data):
        self.canvas = analysis_canvas
        self.patient_data = patient_data
        self.reference_data = reference_data

    def displayPSD(self):
        fig, ax = plt.subplots(figsize=(8, 4))

        # Plot patient PSD
        patient_freqs, patient_psd = scipy.signal.welch(self.patient_data, fs=200)
        patient_psd = patient_psd.squeeze()  # Remove extra dimensions
        patient_psd = np.where(patient_psd <= 0, 1e-10, patient_psd)  # Set zero or negative values to a small positive value
        ax.plot(patient_freqs, 10 * np.log10(patient_psd), label="Patient PSD")

        # Resize reference data to match patient data length
        reference_data_resized = np.interp(
            np.linspace(0, 1, num=len(self.patient_data)),
            np.linspace(0, 1, num=len(self.reference_data)),
            self.reference_data
        )

        # Plot reference PSD
        reference_freqs, reference_psd = scipy.signal.welch(reference_data_resized, fs=200)
        reference_psd = reference_psd.squeeze()  # Remove extra dimensions
        reference_psd = np.where(reference_psd <= 0, 1e-10, reference_psd)  # Set zero or negative values to a small positive value
        ax.plot(reference_freqs, 10 * np.log10(reference_psd), label="Reference PSD")

        ax.set_title("Power Spectral Density")
        ax.set_xlabel("Frequency (Hz)")
        ax.set_ylabel("Power Spectral Density (dB/Hz)")
        ax.legend()

        # Create a Tkinter canvas and display the figure on it
        canvas = FigureCanvasTkAgg(fig, master=self.canvas)
        canvas.draw()

        # Pack the canvas into the Tkinter window
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Store the canvas reference
        self.canvas = canvas




























