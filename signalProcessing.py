import pandas
import scipy
import numpy

class signal:
    def __init__(self, data: pandas.DataFrame):
        self.data = data
        
    def applyFourierTransform(self):
        signal = self.data.iloc[:, 0]
        transformedSignal = scipy.fft.fft(signal)
        transformedSignal = numpy.delete(transformedSignal, 0)
        transformedSignal_shifted = scipy.fft.fftshift(transformedSignal)
        frequencies = scipy.fft.fftfreq(transformedSignal_shifted.size, d=0.1)
        return scipy.fft.fftshift(frequencies), self.__normaliseSpectrum(transformedSignal_shifted)
    
    def __normaliseSpectrum(self, transformedSignal: numpy.ndarray) -> numpy.ndarray:
        percentile = numpy.percentile(transformedSignal, 90)
        for i in range(len(transformedSignal)):
            if transformedSignal[i] < percentile:
                transformedSignal[i] = 0
        return abs(transformedSignal)