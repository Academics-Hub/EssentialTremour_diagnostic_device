import tkinter
import customtkinter
import patient
import plot
import csvHandling

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()
root.title("Essential Tremor Analysis")
colour = "#2A2A2A"
plot_canvas = tkinter.Canvas(root, bd=0, bg=colour, highlightthickness=0)
analysis_canvas = tkinter.Canvas(root, bd=0, bg=colour, highlightthickness=0)
def getCSV():
    file = customtkinter.filedialog.askopenfilename()
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
buttonFrame = customtkinter.CTkFrame(root)
buttonFrame.pack(side=tkinter.TOP, pady=10, padx=10)
importButton = customtkinter.CTkButton(buttonFrame, text="Import CSV File and plot data", command=getCSV)
importButton.pack(side=tkinter.LEFT, pady=10, padx=10)
plotButton = customtkinter.CTkButton(buttonFrame, text="Record patient data", command=patientRecordOnClick)
plotButton.pack(side=tkinter.LEFT, pady=10, padx=10)
#plot canvas
plot_canvas.pack(expand=True, side=tkinter.TOP, padx=5, pady=5, fill=tkinter.BOTH )
#analysis canvas
analysis_canvas.pack(expand=True, side=tkinter.BOTTOM, padx=5, pady=5, fill=tkinter.BOTH )
analysis_canvas.create_text(20, 20, font="Times 30 bold", anchor=tkinter.NW, text="Analysis", fill="white")
root.mainloop()