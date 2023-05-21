import pandas as pd
import scipy.fft
import numpy as np

class Signal:
    def __init__(self, data):
        self.data = data

    def applyFourierTransform(self):
        if isinstance(self.data, str):
            data = pd.read_csv(self.data)  # Read data from file
            signal = data.iloc[:, 0]
        else:
            signal = self.data.iloc[:, 0]  # Assume data is already a DataFrame

        transformedSignal = scipy.fft.fft(signal)
        transformedSignal = np.delete(transformedSignal, 0)
        transformedSignal_shifted = scipy.fft.fftshift(transformedSignal)
        frequencies = scipy.fft.fftfreq(transformedSignal_shifted.size, d=0.001)
        return scipy.fft.fftshift(frequencies), transformedSignal_shifted

    def _normaliseSpectrum(self, transformedSignal):
        percentile = np.percentile(transformedSignal, 90)
        for i in range(len(transformedSignal)):
            if transformedSignal[i] < percentile:
                transformedSignal[i] = 0
        return np.abs(transformedSignal)

    @staticmethod
    def calculateCrossSpectralDensity(signal1, signal2):
        min_length = min(len(signal1), len(signal2))
        signal1 = signal1[:min_length]
        signal2 = signal2[:min_length]
        return np.multiply(signal1, np.conj(signal2))






