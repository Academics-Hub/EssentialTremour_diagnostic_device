import tkinter
import pandas
import signalProcessing

class Analysis:
    def __init__(self, canvas: tkinter.Canvas, data: pandas.DataFrame):
        self.canvas = canvas
        self.time_signal = data
        self.frequency_signal = signalProcessing.signal(data).applyFourierTransform()
        self.csd = signalProcessing.crossSpectralDensity(self.frequency_signal)

    def displayCSD(self):
        window = tkinter.Toplevel()
        window.title("Cross Spectral Density")

        canvas = tkinter.Canvas(window, width=800, height=600)
        canvas.pack()

        canvas.create_line(50, 50, 750, 50, width=2)  
        canvas.create_line(50, 50, 50, 550, width=2)  
        canvas.create_text(400, 30, text="Cross Spectral Density", font=("Arial", 20))

        x_scale = 700 / (self.csd.shape[0] - 1)
        y_scale = 500 / (self.csd.max() - self.csd.min())
        for i in range(self.csd.shape[0] - 1):
            x1 = 50 + i * x_scale
            y1 = 550 - (self.csd[i] - self.csd.min()) * y_scale
            x2 = 50 + (i + 1) * x_scale
            y2 = 550 - (self.csd[i + 1] - self.csd.min()) * y_scale
            canvas.create_line(x1, y1, x2, y2, width=2, fill="blue")

        window.mainloop()
