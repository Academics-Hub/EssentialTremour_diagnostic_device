import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np
import scipy.signal
from scipy import signal

class Analysis:
    def __init__(self, patient_data, reference_data, psd_canvas, report_canvas):
        self.patient_data = patient_data
        self.reference_data = reference_data
        self.report_canvas = report_canvas
        self.psd_canvas = psd_canvas
        self.patient_freqs = None

    def displayPSD(self):
        fig, ax = plt.subplots(figsize=(8, 4))

        # Reshape patient data
        patient_data = self.patient_data.reshape(-1)

        # Calculate patient PSD and assign frequency values to self.patient_freqs
        self.patient_freqs, patient_psd = scipy.signal.welch(patient_data, fs=200)

        # Plot patient PSD
        patient_freqs, patient_psd = scipy.signal.welch(patient_data, fs=200)
        patient_psd = patient_psd.squeeze()  # Remove extra dimensions
        patient_psd = np.where(patient_psd <= 0, 1e-10, patient_psd)  # Set zero or negative values to a small positive value
        ax.plot(patient_freqs, 10 * np.log10(patient_psd), label="Patient PSD")

        # Resize reference data to match patient data length
        reference_data_resized = np.interp(
            np.linspace(0, 1, num=len(self.patient_data)),
            np.linspace(0, 1, num=len(self.reference_data)),
            self.reference_data
        )

        # Reshape reference data
        reference_data_resized = reference_data_resized.reshape(-1)

        # Plot reference PSD
        reference_freqs, reference_psd = scipy.signal.welch(reference_data_resized, fs=200)
        reference_psd = reference_psd.squeeze()  # Remove extra dimensions
        reference_psd = np.where(reference_psd <= 0, 1e-10, reference_psd)  # Set zero or negative values to a small positive value
        ax.plot(reference_freqs, 10 * np.log10(reference_psd), label="Reference PSD")

        #ax.set_title("Power Spectral Density")
        ax.set_xlim([0, 30])
        ax.set_xlabel("Frequency (Hz)")
        ax.set_ylabel("Power Spectral Density (dB/Hz)")
        ax.legend()

        # Create a Tkinter canvas and display the figure on it
        self.psd_canvas = FigureCanvasTkAgg(fig, master=self.psd_canvas)
        self.psd_canvas.draw()

        # Embed the figure canvas within the psd_canvas
        self.psd_canvas.get_tk_widget().place(relx=0, rely=0, relwidth=1, relheight=1)


    def analyze_psd(self):
        # Perform your PSD analysis and compare with the reference PSD

        # Calculate the patient PSD using scipy.signal.welch
        patient_freqs, patient_psd = scipy.signal.welch(self.patient_data, fs=200)

        # Calculate the reference PSD using scipy.signal.welch
        reference_freqs, reference_psd = scipy.signal.welch(self.reference_data, fs=200)

        # Define the frequency range for essential tremors
        tremor_frequency_range = (4, 12)  # Hz

        # Get the indices corresponding to the frequency range
        freq_indices = np.where((patient_freqs >= tremor_frequency_range[0]) &
                                (patient_freqs <= tremor_frequency_range[1]))[0]

        # Get the PSD values within the frequency range
        patient_psd_range = patient_psd[freq_indices]
        reference_psd_range = reference_psd[freq_indices]

        # Compare the patient PSD with the reference PSD
        has_essential_tremor = np.max(patient_psd_range) > np.max(reference_psd_range)

        # Find the peak frequencies within the tremor frequency range
        peak_indices = scipy.signal.find_peaks(patient_psd_range, prominence=1)[0]
        peak_frequencies = patient_freqs[freq_indices][peak_indices]

        return has_essential_tremor, peak_frequencies


    def generate_patient_report(self, patient_name, has_essential_tremor, peak_frequencies):
        report = f"Patient Report for {patient_name}\n\n"

        # Configure formatting options
        heading_font = ("Arial", 16, "bold")
        body_font = ("Arial", 12)
        bullet_point = "  \u2022 "  # Bullet point character

        if has_essential_tremor:
            report += "Observations:\n"
            report += bullet_point + "The patient exhibits characteristics consistent with essential tremor.\n"
            report += bullet_point + "Significant peaks were observed in the following frequency range(s):\n"
            for frequency in peak_frequencies:
                report += bullet_point + f"{frequency:.2f} Hz\n"
        else:
            report += "Diagnosis: No Essential Tremor Detected\n"
            report += "\n"
            report += "Observations:\n"
            report += "  " + bullet_point + "The patient does not exhibit characteristics consistent with essential tremor.\n"

        return report


    def generate_report_and_display(self, patient_name, report_canvas):
        # Perform PSD analysis and obtain essential tremor diagnosis and peak frequencies
        has_essential_tremor, peak_frequencies = self.analyze_psd()

        # Generate the patient report
        report = self.generate_patient_report(patient_name, has_essential_tremor, peak_frequencies)

        # Clear the existing content of the report canvas
        report_canvas.delete(tk.ALL)

        # Create a text object on the report canvas to display the report
        report_canvas.create_text(20, 20, anchor=tk.NW, text=report, fill="white")





