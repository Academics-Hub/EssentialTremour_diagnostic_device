import pandas as pd
import scipy.fft
import numpy as np
from scipy import signal

class Signal:
    def __init__(self, data: pd.DataFrame):
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

    def _antialisingFilter(self) -> pd.DataFrame:
        filter_high = signal.cheby1(12, 1, [3.8, 100], 'bp', fs=1000, output='sos')
        filteredSignal = signal.sosfilt(filter_high, self.data)
        return pd.DataFrame(filteredSignal)
        

    @staticmethod
    def calculateCrossSpectralDensity(signal1, signal2):
        min_length = min(len(signal1), len(signal2))
        signal1 = signal1[:min_length]
        signal2 = signal2[:min_length]
        return np.multiply(signal1, np.conj(signal2))






