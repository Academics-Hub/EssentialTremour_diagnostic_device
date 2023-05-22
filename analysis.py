import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np
import scipy.signal

class Analysis:
    def __init__(self, patient_data, reference_data, canvas):
        self.patient_data = patient_data
        self.reference_data = reference_data
        self.canvas = canvas

    def displayPSD(self):
        fig, ax = plt.subplots(figsize=(8, 4))

        # Reshape patient data
        patient_data = self.patient_data.reshape(-1)

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

        ax.set_title("Power Spectral Density")
        ax.set_xlabel("Frequency (Hz)")
        ax.set_ylabel("Power Spectral Density (dB/Hz)")
        ax.legend()

        # Create a Tkinter canvas and display the figure on it
        self.canvas = FigureCanvasTkAgg(fig, master=self.canvas)
        self.canvas.draw()

        # Pack the canvas into the Tkinter window
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)


    def analyze_psd(self):
        # Perform your PSD analysis and compare with the reference PSD
            
        # Define the frequency range for essential tremors
        tremor_frequency_range = (4, 12)  # Hz
            
        # Get the indices corresponding to the frequency range
        freq_indices = np.where((self.patient_freqs >= tremor_frequency_range[0]) &
                                (self.patient_freqs <= tremor_frequency_range[1]))[0]
            
        # Get the PSD values within the frequency range
        patient_psd_range = self.patient_psd[freq_indices]
        reference_psd_range = self.reference_psd[freq_indices]
            
        # Compare the patient PSD with the reference PSD
        has_essential_tremor = np.max(patient_psd_range) > np.max(reference_psd_range)
            
        # Find the peak frequencies within the tremor frequency range
        peak_indices = scipy.signal.find_peaks(patient_psd_range, prominence=1)[0]
        peak_frequencies = self.patient_freqs[freq_indices][peak_indices]
            
        return has_essential_tremor, peak_frequencies

    def generate_patient_report(self, patient_name, has_essential_tremor, peak_frequencies):
        report = f"Patient Report for {patient_name}\n\n"

        if has_essential_tremor:
            report += "Diagnosis: Essential Tremor\n"
            report += "Observations:\n"
            report += "- The patient exhibits characteristics consistent with essential tremor.\n"
            report += "- Significant peaks were observed in the following frequency range(s):\n"
            for frequency in peak_frequencies:
                report += f"  - {frequency:.2f} Hz\n"
        else:
            report += "Diagnosis: No Essential Tremor Detected\n"
            report += "Observations:\n"
            report += "- The patient does not exhibit characteristics consistent with essential tremor.\n"

        return report

    def generate_report_and_display(self, patient_name):
        # Perform PSD analysis and obtain essential tremor diagnosis and peak frequencies
        has_essential_tremor, peak_frequencies = self.analyze_psd()

        # Generate the patient report
        report = self.generate_patient_report(patient_name, has_essential_tremor, peak_frequencies)

        # Clear the existing content of the text widget
        self.text.delete("1.0", tk.END)

        # Append the patient report to the text widget
        self.text.insert(tk.END, report)

        # Display the power spectral density
        self.displayPSD()

