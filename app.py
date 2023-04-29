import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import arduino as a
from tkinter import Label
import time

root = tk.Tk()

root.title("Essential Tremor Analysis")
#root.state('zoomed')

canvas1 = tk.Canvas(root)
canvas1.pack(fill=tk.BOTH, expand=True)

# Create a menu bar and add it to the root window
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Create a "File" menu and add it to the menu bar
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Menu", menu=file_menu)

def getCSV():
    global df
    import_file_path = filedialog.askopenfilename()
    df = pd.read_csv(import_file_path)

    # Display a success message after importing the CSV file
    messagebox.showinfo("Success", "CSV file imported successfully")
    plotData(10)

# Add a command to the "File" menu to import a CSV file
file_menu.add_command(label="Import CSV File and plot data", command=getCSV)


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
    linePlot1 = FigureCanvasTkAgg(figure1, root)
    linePlot1.get_tk_widget().place(relx=0.3, rely=0.3, anchor=tk.CENTER, relwidth=0.5, relheight=0.6)
    # Plot the real part of the Fourier transform
    ax2.plot(frequencies, abs(fourier_transform))
    ax2.set_title('Normalized frequency spectrum, \ndisplaying spikes in the \n90th percentile of frequencies')
    ax2.set_xlabel('frequency (Hz)')
    ax2.set_yticks([])
    linePlot2 = FigureCanvasTkAgg(figure2, root)
    linePlot2.get_tk_widget().place(relx=0.7, rely=0.3, anchor=tk.CENTER, relwidth=0.5, relheight=0.6)

file_menu.add_command(label="Plot data", command=plotData)

def countdown(count, label):
    label['text'] = count
    if count > 0:
        root.after(1000, countdown, count-1)
        
def patientData():
    timer = 10
    global df
    arduino = a.arduino('/dev/ttyACM0', 9600)
    arduino.read('data.csv', timer)
    df = pd.read_csv('data.csv')
    messagebox.showinfo("Success", "Patient data read successfully")
    plotData(timer)
    
    timer_window = tk.Toplevel(root)
    timer_window.geometry("200x100")      
    label = tk.Label(timer_window, text="Please wait while patient data is read")
    label.pack()
    
    countdown(timer, label)

file_menu.add_command(label="Record patient data", command=patientData)

root.mainloop()