import tkinter as tk
import customtkinter
import csvHandling
from analysis import Analysis
import patient
from plot import Plot
import numpy as np
import os

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()
root.title("Essential Tremor Analysis")
colour = "#2A2A2A"
report_canvas = tk.Canvas(root, bd=0, bg=colour, highlightthickness=0)
signal_canvas = tk.Canvas(root, bd=0, bg=colour, highlightthickness=0)
analysis_canvas = tk.Canvas(root, bd=0, bg=colour, highlightthickness=0)
analysis_obj = None
data = None  # Global variable for data

def getCSV():
    global analysis_obj, data  # Declare data as a global variable

    # Open a file dialog to select the patient's data CSV file
    file_path = customtkinter.filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])

    if file_path:
        # Read the patient's data CSV file
        csv = csvHandling.Csv(file_path)
        data = csv.read()

        # Trim or interpolate the patient's data to match the desired length (10 seconds)
        desired_length = 300  # Assuming 200 samples per second (10 seconds * 200 samples/s)
        if len(data) > desired_length:
            data = data[:desired_length]
        elif len(data) < desired_length:
            # Perform linear interpolation manually
            old_indices = np.arange(len(data))
            new_indices = np.linspace(0, len(data) - 1, desired_length)
            print("Before interpolation - data shape:", data.shape)
            print("Before interpolation - new_indices shape:", new_indices.shape)
            data = np.interp(new_indices, old_indices, data)
            print("After interpolation - data shape:", data.shape)

        # Read the reference data CSV file
        reference_csv = csvHandling.Csv("ref.csv")
        reference_data = reference_csv.read()

        # Trim or interpolate the reference data to match the desired length (10 seconds)
        if len(reference_data) > desired_length:
            reference_data = reference_data[:desired_length]
        elif len(reference_data) < desired_length:
            # Perform linear interpolation manually
            old_indices = np.arange(len(reference_data))
            new_indices = np.linspace(0, len(reference_data) - 1, desired_length)
            print("Before interpolation - reference_data shape:", reference_data.shape)
            print("Before interpolation - new_indices shape:", new_indices.shape)
            reference_data = np.interp(new_indices, old_indices, reference_data)
            print("After interpolation - reference_data shape:", reference_data.shape)

        analysis_obj = Analysis(data, reference_data, analysis_canvas, report_canvas)
        recording_time = csv.readingTime()
        plot_obj = Plot(signal_canvas, data, recording_time)

        # Display the original signal on the signal canvas
        plot_obj.createPatientPlot()

        # Get the patient's name from the CSV file
        patient_name = os.path.splitext(os.path.basename(file_path))[0]

        # Display the PSD and generate the report
        displayPSDAndGenerateReport(patient_name)


def displayPSDAndGenerateReport(patient_name):
    global analysis_obj, report_canvas

    # Display the power spectral density on the analysis canvas
    analysis_obj.displayPSD()

    # Generate the report and display it on the report canvas
    analysis_obj.generate_report_and_display(patient_name, report_canvas)


def patientRecordOnClick():
    p = patient.Patient()
    p.recordPatient()
    patientPlot = plot.Plot(plot_canvas, p.getData(), p.getTime())
    patientPlot.createPatientPlot()

# Buttons to carry out functionality
buttonFrame = customtkinter.CTkFrame(root)
buttonFrame.pack(side=tk.TOP, pady=10, padx=10)
importButton = customtkinter.CTkButton(buttonFrame, text="Import CSV File and plot data", command=getCSV)
importButton.pack(side=tk.LEFT, pady=10, padx=10)
plotButton = customtkinter.CTkButton(buttonFrame, text="Record patient data", command=patientRecordOnClick)
plotButton.pack(side=tk.LEFT, pady=10, padx=10)

# Original signal container
signal_container = tk.LabelFrame(root, text="Original Signal", font="Times 30 bold", fg="white", bg=colour)
signal_container.pack(expand=True, side=tk.TOP, padx=5, pady=5, fill=tk.BOTH)

# Original signal canvas
signal_canvas = tk.Canvas(signal_container, bd=0, bg=colour, highlightthickness=0)
signal_canvas.pack(expand=True, fill=tk.BOTH)

# Analysis container
analysis_container = tk.LabelFrame(root, text="Power Spectral Density", font="Times 30 bold", fg="white", bg=colour)
analysis_container.pack(expand=True, side=tk.TOP, padx=5, pady=5, fill=tk.BOTH)

# Analysis canvas
analysis_canvas = tk.Canvas(analysis_container, bd=0, bg=colour, highlightthickness=0)
analysis_canvas.pack(expand=True, fill=tk.BOTH)

# Report container
report_container = tk.LabelFrame(root, text="Paitient Report", font="Times 30 bold", fg="white", bg=colour)
report_container.pack(expand=True, side=tk.TOP, padx=5, pady=5, fill=tk.BOTH)

# Report canvas
report_canvas = tk.Canvas(report_container, bd=0, bg=colour, highlightthickness=0)
report_canvas.pack(expand=True, fill=tk.BOTH)

root.mainloop()


