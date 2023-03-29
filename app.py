import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import arduino as a

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
    fourier_transform = np.fft.fft(signal)

    # Shift the zero-frequency component to the center of the spectrum
    fourier_transform_shifted = np.fft.fftshift(fourier_transform)

    # Calculate the frequencies for each element in the Fourier Transform
    sample_rate = 1 / (time[1] - time[0])
    frequencies = np.fft.fftfreq(len(fourier_transform), d=1/sample_rate)

    return frequencies, fourier_transform_shifted

def plotData():
    frequencies, fourier_transform = applyFourierTransform()
    figure1 = plt.Figure(figsize=(5,5), dpi=100)
    figure2 = plt.Figure(figsize=(5,5), dpi=100)
    ax1 = figure1.add_subplot(1, 1, 1)
    ax2 = figure2.add_subplot(1, 1, 1)

    # plot original signal
    ax1.plot(df.iloc[:, 0], df.iloc[:, 1])
    ax1.set_title('original signal')
    linePlot1 = FigureCanvasTkAgg(figure1, root)
    linePlot1.get_tk_widget().place(relx=0.3, rely=0.3, anchor=tk.CENTER, relwidth=0.4, relheight=0.5)
    # Plot the real part of the Fourier transform
    ax2.stem(np.fft.fftshift(frequencies), abs(fourier_transform))
    ax2.set_title('frequency spectra')
    linePlot2 = FigureCanvasTkAgg(figure2, root)
    linePlot2.get_tk_widget().place(relx=0.7, rely=0.3, anchor=tk.CENTER, relwidth=0.4, relheight=0.5)

file_menu.add_command(label="Plot data", command=plotData)

def createCSV():
    a.read('data.csv')
    messagebox.showinfo("Success", "Patient data read successfully")
       

file_menu.add_command(label="Record patient data", command=createCSV)

root.mainloop()