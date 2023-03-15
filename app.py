import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from numpy.fft import fft
import arduino as a

root = tk.Tk()

root.title("Essential Tremor Analysis")
root.wm_attributes('-zoomed', True)

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
    print(df)

    # Display a success message after importing the CSV file
    messagebox.showinfo("Success", "CSV file imported successfully")

# Add a command to the "File" menu to import a CSV file
file_menu.add_command(label="Import CSV File", command=getCSV)

def applyFourierTransform():
    # Get the time and signal data from the DataFrame
    time = df.iloc[:, 0]
    signal = df.iloc[:, 1]

    # Apply the Fourier Transform to the signal data
    fourier_transform = fft(signal)

    # Shift the zero-frequency component to the center of the spectrum
    fourier_transform_shifted = np.fft.fftshift(fourier_transform)

    # Calculate the frequencies for each element in the Fourier Transform
    sample_rate = 1 / (time[1] - time[0])
    frequencies = fft.fftfreq(len(fourier_transform), d=1/sample_rate)
    frequencies_shifted = fft.fftshift(frequencies)

    return frequencies_shifted, fourier_transform_shifted

def plotData():
    frequencies, fourier_transform = applyFourierTransform()
    figure1 = plt.Figure(figsize=(3,3), dpi=100)
    ax1 = figure1.add_subplot(111)

    # Plot the real part of the Fourier transform
    ax1.plot(df.iloc[:, 0], abs(fourier_transform))
    ax1.set_title('Real Part')
    linePlot1 = FigureCanvasTkAgg(figure1, root)
    linePlot1.get_tk_widget().place(relx=0.2, rely=0.2, anchor=tk.CENTER, relwidth=0.3, relheight=0.3)

    figure2 = plt.Figure(figsize=(3,3), dpi=100)
    ax2 = figure2.add_subplot(111)

    # Plot the frequency spectrum of the Fourier transform
    ax2.stem(frequencies, np.abs(df[df.columns[2]]))
    ax2.set_title('Frequency Spectrum')
    linePlot2 = FigureCanvasTkAgg(figure2, root)
    linePlot2.get_tk_widget().place(relx=0.5, rely=0.2, anchor=tk.CENTER, relwidth=0.3, relheight=0.3)

file_menu.add_command(label="Plot data", command=plotData)

def createCSV():
    a.read('data.csv')
    messagebox.showinfo("Success", "Patient data read successfully")
       

file_menu.add_command(label="Record patient data", command=createCSV)

root.mainloop()