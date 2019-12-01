from Calculator.Calculator import Calculator
from Statistics.Mean import mean
from Statistics.Median import median
from Statistics.Mode import mode
from Statistics.Variance import variance
from Statistics.pVariance import pvariance
from Statistics.StandardDeviation import standarddeviation
from Statistics.SampleMean import sample_mean
from Statistics.zscore import zscore
from CSVReader.CsvReader import CsvReader


class Statistics(Calculator):
    data = []

    def __init__(self):
        pass

    def mean(self, val1, val2, val3, val4, val5, val6, val7, val8, val9, val10):
        self.result = mean(val1, val2, val3, val4, val5, val6, val7, val8, val9, val10)
        return self.result

    def sample_mean(self, val1, val2, val3, val4, val5):
        self.result = sample_mean(val1, val2, val3, val4, val5)
        return self.result

    def median(self, val1, val2, val3, val4, val5, val6, val7, val8, val9):
        self.result = median(val1, val2, val3, val4, val5, val6, val7, val8, val9)
        return self.result

    def mode(self, val1, val2, val3, val4, val5, val6, val7, val8, val9, val10):
        self.result = mode(val1, val2, val3, val4, val5, val6, val7, val8, val9, val10)
        return self.result

    def variance(self, val1, val2, val3, val4, val5, val6, val7, val8, val9, val10):
        self.result = variance(val1, val2, val3, val4, val5, val6, val7, val8, val9, val10)
        return self.result

    def pvariance(self, val1, val2, val3, val4, val5, val6, val7, val8, val9, val10):
        self.result = pvariance(val1, val2, val3, val4, val5, val6, val7, val8, val9, val10)
        return self.result

    def standarddeviation(self, val1, val2, val3, val4, val5, val6, val7, val8, val9, val10):
        self.result = standarddeviation(val1, val2, val3, val4, val5, val6, val7, val8, val9, val10)
        return self.result

    def zscore(self, a, b, c):
        self.result = zscore(a, b, c)
        return self.result
