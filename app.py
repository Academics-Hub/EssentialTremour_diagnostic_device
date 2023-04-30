import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import recordPatient

root = tk.Tk()
root.title("Essential Tremor Analysis")

def getCSV():
    global df
    import_file_path = filedialog.askopenfilename()
    df = pd.read_csv(import_file_path)

    # Display a success message after importing the CSV file
    messagebox.showinfo("Success", "CSV file imported successfully")
    plotData(10)

def patientRecordOnClick():
    patient = recordPatient.patient("test")
    patient.recordPatient()

# Add a command to the "File" menu to import a CSV file
buttonFrame = tk.Frame(root)
buttonFrame.pack(side=tk.TOP, pady=10, padx=10)
importButton = tk.Button(buttonFrame, text="Import CSV File and plot data", command=getCSV)
importButton.pack(side=tk.LEFT, pady=10, padx=10)
plotButton = tk.Button(buttonFrame, text="Record patient data", command=patientRecordOnClick)
plotButton.pack(side=tk.LEFT, pady=10, padx=10)


def applyFourierTransform():
    # Get the signal data from the DataFrame
    signal = df.iloc[:, 0]
    #first account for noise and shift up by 55
    for i in range(len(signal)):
        signal[i] = signal[i] + 55

    # Apply the Fourier Transform to the signal data
    fourier_transform = np.fft.fft(signal)

    # filter out the massive noise spike at 0Hz
    fourier_transform = np.delete(fourier_transform, 0)
    # Shift the zero-frequency component to the center of the spectrum
    fourier_transform_shifted = np.fft.fftshift(fourier_transform)

    # Calculate the frequencies for each element in the Fourier Transform
    
    frequencies = np.fft.fftfreq(fourier_transform_shifted.size, d=0.1)

    return np.fft.fftshift(frequencies), normaliseSpectrum(fourier_transform_shifted)

def normaliseSpectrum(fourier_transform: np.ndarray) -> np.ndarray:
    #find the 90% percentile of the data
    percentile = np.percentile(fourier_transform, 90)
    #if value above percentile keep it, if not, discard it
    for i in range(len(fourier_transform)):
        if fourier_transform[i] < percentile:
            fourier_transform[i] = 0
    return fourier_transform

canvas = tk.Canvas(root)
canvas.pack(anchor=tk.S, expand=True, side=tk.BOTTOM, ipadx=10, ipady=10, fill=tk.BOTH)

def plotData(time):
    frequencies, fourier_transform = applyFourierTransform()
    figure1 = plt.Figure(figsize=(5,5), dpi=100)
    figure2 = plt.Figure(figsize=(5,5), dpi=100)
    ax1 = figure1.add_subplot(1, 1, 1)
    ax2 = figure2.add_subplot(1, 1, 1)

    # plot original signal
    ax1.plot(np.arange(len(df.iloc[:, 0])), df.iloc[:, 0])
    ax1.set_title('Recorded change in acceleration')
    ax1.set_xlabel('time (' + str(time) + 's)')
    ax1.set_ylabel('Amplitude (m/s^2)')
    ax1.set_xticks([])
    linePlot1 = FigureCanvasTkAgg(figure1, canvas)
    linePlot1.get_tk_widget().place(relx=0.3, rely=0.5, anchor=tk.CENTER, relwidth=0.5, relheight=0.6)
    # Plot the real part of the Fourier transform
    ax2.plot(frequencies, abs(fourier_transform))
    ax2.set_title('Normalized frequency spectrum, \ndisplaying spikes in the \n90th percentile of frequencies')
    ax2.set_xlabel('frequency (Hz)')
    ax2.set_yticks([])
    linePlot2 = FigureCanvasTkAgg(figure2, canvas)
    linePlot2.get_tk_widget().place(relx=0.7, rely=0.5, anchor=tk.CENTER, relwidth=0.5, relheight=0.6)

root.mainloop()