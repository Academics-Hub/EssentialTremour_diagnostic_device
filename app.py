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
    patientPlot = plot.Plot(canvas, data)
    patientPlot.createPatientPlot()

def patientRecordOnClick():
    patient = recordPatient.patient("test")
    patient.recordPatient()
    patientPlot = plot.Plot(canvas, data)
    patientPlot.createPatientPlot()

buttonFrame = tkinter.Frame(root)
buttonFrame.pack(side=tkinter.TOP, pady=10, padx=10)
importButton = tkinter.Button(buttonFrame, text="Import CSV File and plot data", command=getCSV)
importButton.pack(side=tkinter.LEFT, pady=10, padx=10)
plotButton = tkinter.Button(buttonFrame, text="Record patient data", command=patientRecordOnClick)
plotButton.pack(side=tkinter.LEFT, pady=10, padx=10)

canvas = tkinter.Canvas(root)
canvas.pack(anchor=tkinter.S, expand=True, side=tkinter.BOTTOM, ipadx=10, ipady=10, fill=tkinter.BOTH)

root.mainloop()