from Statistics.Variance import variance
from Calculator.Sqrt import sqrt


def standarddeviation(val1, val2, val3, val4, val5, val6, val7, val8, val9, val10):
    try:
        standarddeviation_values = [val1, val2, val3, val4, val5, val6, val7, val8, val9, val10]
        standarddeviation_float = [float(i) for i in standarddeviation_values]
        return sqrt(variance(*standarddeviation_float))
    except TypeError:
        print("std dev is a Number . Cannot Input Text")
