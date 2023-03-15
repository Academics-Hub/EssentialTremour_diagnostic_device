import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from numpy.fft import fft, fftshift

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

def plotData():
    figure1 = plt.Figure(figsize=(3,3), dpi=100)
    ax1 = figure1.add_subplot(111)

    # Plot the real part of the Fourier transform
    ax1.plot(df[df.columns[0]], df[df.columns[1]])
    ax1.set_title('Real Part')
    linePlot1 = FigureCanvasTkAgg(figure1, root)
    linePlot1.get_tk_widget().place(relx=0.2, rely=0.2, anchor=tk.CENTER, relwidth=0.3, relheight=0.3)

    figure2 = plt.Figure(figsize=(3,3), dpi=100)
    ax2 = figure2.add_subplot(111)

    # Plot the frequency spectrum of the Fourier transform
    freqs = np.fft.fftfreq(len(df[df.columns[0]]), d=0.1)
    ax2.stem(freqs, np.abs(df[df.columns[2]]))
    ax2.set_title('Frequency Spectrum')
    linePlot2 = FigureCanvasTkAgg(figure2, root)
    linePlot2.get_tk_widget().place(relx=0.5, rely=0.2, anchor=tk.CENTER, relwidth=0.3, relheight=0.3)

    figure3 = plt.Figure(figsize=(3,3), dpi=100)
    ax3 = figure3.add_subplot(111)

    # Plot the phase spectrum of the Fourier transform
    phase_spectrum = np.angle(df[df.columns[2]])
    ax3.stem(freqs, phase_spectrum)
    ax3.set_title('Phase Spectrum')
    linePlot3 = FigureCanvasTkAgg(figure3, root)
    linePlot3.get_tk_widget().place(relx=0.8, rely=0.2, anchor=tk.CENTER, relwidth=0.3, relheight=0.3)

file_menu.add_command(label="Plot data", command=plotData)

def createCSV():
    # Define rect(x) function
    def rect(x):
        return np.where(abs(x) < 0.5, 1, 0)
    
    # Create an array from 0 to 10 with step size of 0.1
    x = np.arange(0, 10, 0.1)
    
    # Apply rect(x) function to each element of x
    result = [rect(i) for i in x]
    
    # Compute Fourier transform of result
    fourier_result = fft(result)
    
    # Apply Fourier shift to fourier_result
    shifted_fourier_result = fftshift(fourier_result)
    shifted_fourier_result = abs(shifted_fourier_result)
    
    # Create a new DataFrame with the shifted Fourier transform result and save it as a CSV file
    result_df = pd.DataFrame(shifted_fourier_result)
    result_df.to_csv("rect_shifted_fourier_transform.csv", index=False)
    
    # Create success window
    success_window = tk.Toplevel(root)
    success_window.title("Success")
    
    success_label = tk.Label(success_window, text="CSV file created successfully!")
    success_label.pack()

file_menu.add_command(label="Create CSV File", command=createCSV)

root.mainloop()