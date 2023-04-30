import tkinter
import pandas
import recordPatient
import plot

root = tkinter.Tk()
root.title("Essential Tremor Analysis")

def getCSV():
    global data
    import_file_path = tkinter.filedialog.askopenfilename()
    data = pandas.read_csv(import_file_path)
    tkinter.messagebox.showinfo("Success", "CSV file imported successfully")
    patientPlot = plot.Plot(plot_canvas, data)
    patientPlot.createPatientPlot()

def patientRecordOnClick():
    patient = recordPatient.patient("test")
    patient.recordPatient()
    patientPlot = plot.Plot(plot_canvas, data)
    patientPlot.createPatientPlot()
#buttons to carry out functionality
buttonFrame = tkinter.Frame(root)
buttonFrame.pack(side=tkinter.TOP, pady=10, padx=10)
importButton = tkinter.Button(buttonFrame, text="Import CSV File and plot data", command=getCSV)
importButton.pack(side=tkinter.LEFT, pady=10, padx=10)
plotButton = tkinter.Button(buttonFrame, text="Record patient data", command=patientRecordOnClick)
plotButton.pack(side=tkinter.LEFT, pady=10, padx=10)
#plot canvas
plot_canvas = tkinter.Canvas(root)
plot_canvas.pack(anchor=tkinter.S, expand=True, side=tkinter.TOP, padx=5, pady=5, fill=tkinter.BOTH )
root.mainloop()