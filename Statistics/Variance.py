from Calculator.Squared import squared
from Calculator.Division import division
from Statistics.Mean import mean
from Calculator.Subtraction import subtraction


def variance(val1, val2, val3, val4, val5, val6, val7, val8, val9, val10):
    try:
        variance_values = [val1, val2, val3, val4, val5, val6, val7, val8, val9, val10]
        variance_float = [float(i) for i in variance_values]
        variance_mean = mean(*variance_float)
        variance_length = len(variance_float)
        x = 0
        for i in variance_float:
            x = x + squared(i-variance_mean)
        return division(x, subtraction(variance_length, 1))
    except TypeError:
        print("Median is a Number . Cannot Input Text")