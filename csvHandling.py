import pandas
import os
import signalProcessing
import numpy

class Csv:
    def __init__(self, filename: str):
        self.filename = filename
        self.data = self.__read()
        self.signal = signalProcessing.Signal(self.data)
    
    def __read(self) -> pandas.DataFrame:
        data = pandas.read_csv(self.filename)
        return data.iloc[:, 0].values
    
    def read(self) -> pandas.DataFrame:
        filteredData = self.signal._antialisingFilter()
        return filteredData.iloc[:, 0].values

    def readingTime(self) -> int:
        time: int
        name, ext = os.path.splitext(self.filename)
        name, time = name.rsplit('-', 1)
        return time