import pandas as pd
import scipy.fft
import numpy as np
from scipy import signal

class Signal:
    def __init__(self, data: pd.DataFrame):
        self.data = data

    def _antialisingFilter(self) -> pd.DataFrame:
        filter_band = signal.cheby1(12, 1, [3.8, 100], 'bp', fs=250, output='sos')
        filteredSignal = signal.sosfilt(filter_band, self.data)
        return pd.DataFrame(filteredSignal)
        
    @staticmethod
    def calculateCrossSpectralDensity(signal1, signal2):
        min_length = min(len(signal1), len(signal2))
        signal1 = signal1[:min_length]
        signal2 = signal2[:min_length]
        return np.multiply(signal1, np.conj(signal2))






