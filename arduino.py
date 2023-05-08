import subprocess
from datetime import datetime
import csv
import tkinter as tk
from tkinter import messagebox
import numpy as np
import time as ti

def read(filename):
    # Call the C++ program as a subprocess
    subprocess.call(["./serial_to_csv"])

    # Read the data from the CSV file created by the C++ program
    with open("data.csv", "r") as f:
        data = [int(line.strip()) for line in f]

    # Write the data to the output file
    with open(filename, "w") as f:
        writer = csv.writer(f)
        for value in data:
            writer.writerow([value])

    # Show a message box indicating that the data has been read
    messagebox.showinfo("Data read", "Patient data has been read and saved to " + filename)