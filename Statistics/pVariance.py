from Calculator.Squared import squared
from Calculator.Division import division
from Statistics.Mean import mean


def pvariance(val1, val2, val3, val4, val5, val6, val7, val8, val9, val10):
    try:
        pvariance_values = [val1, val2, val3, val4, val5, val6, val7, val8, val9, val10]
        pvariance_float = [float(i) for i in pvariance_values]
        pvariance_mean = mean(*pvariance_float)
        pvariance_length = len(pvariance_float)
        x = 0
        for i in pvariance_float:
            x = x + squared(i-pvariance_mean)
        population_variance = division(x, pvariance_length)
        return population_variance
    except TypeError:
        print("Population Variance is a Number . Cannot Input Text")
