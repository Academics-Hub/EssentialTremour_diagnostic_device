import tkinter
import pandas
import patient
import plot
import csvHandling

root = tkinter.Tk()
root.title("Essential Tremor Analysis")
plot_canvas = tkinter.Canvas(root)
analysis_canvas = tkinter.Canvas(root)
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
plot_canvas.pack(expand=True, side=tkinter.TOP, padx=5, pady=5, fill=tkinter.BOTH )
#analysis canvas
analysis_canvas.pack(expand=True, side=tkinter.BOTTOM, padx=5, pady=5, fill=tkinter.BOTH )
analysis_canvas.create_text(20, 20, font="Times 30 bold", anchor=tkinter.NW, text="Analysis")
root.mainloop()