import tkinter as tk
import customtkinter
import csvHandling
from analysis import Analysis
import patient
import plot
import numpy as np

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()
root.title("Essential Tremor Analysis")
colour = "#2A2A2A"
plot_canvas = tk.Canvas(root, bd=0, bg=colour, highlightthickness=0)
analysis_canvas = tk.Canvas(root, bd=0, bg=colour, highlightthickness=0)
analysis_obj = None

def getCSV():
    global analysis_obj

    # Open a file dialog to select the patient's data CSV file
    file_path = customtkinter.filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])

    if file_path:
        # Read the patient's data CSV file
        csv = csvHandling.Csv(file_path)
        data = csv.read()

        # Trim or interpolate the patient's data to match the desired length (10 seconds)
        desired_length = 2000  # Assuming 200 samples per second (10 seconds * 200 samples/s)
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

        # Create an instance of the Analysis class
        analysis_obj = Analysis(analysis_canvas, data, reference_data)

        # Display the power spectral density
        analysis_obj.displayPSD()

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

# Plot canvas
plot_canvas.pack(expand=True, side=tk.TOP, padx=5, pady=5, fill=tk.BOTH)

# Analysis canvas
analysis_canvas.pack(expand=True, side=tk.BOTTOM, padx=5, pady=5, fill=tk.BOTH)
analysis_canvas.create_text(20, 20, font="Times 30 bold", anchor=tk.NW, text="Analysis", fill="white")

root.mainloop()
















