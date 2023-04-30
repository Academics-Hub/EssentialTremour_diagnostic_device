import tkinter
import pandas
import patient
import plot
import csvHandling

root = tkinter.Tk()
root.title("Essential Tremor Analysis")

def getCSV():
    file = tkinter.filedialog.askopenfilename()
    csv = csvHandling.Csv(file)
    data = csv.read()
    patientPlot = plot.Plot(plot_canvas, data, csv.readingTime())
    patientPlot.createPatientPlot()

def patientRecordOnClick():
    p = patient.Patient()
    p.recordPatient()
    patientPlot = plot.Plot(plot_canvas, p.getData(), p.getTime())
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