from Calculator.Division import division
from Calculator.Subtraction import subtraction

def zscore(a, b, c):
    score = float(a)
    zmean = float(b)
    zstd = float(c)
    numerator = subtraction(score, zmean)
    zscore = division(numerator, zstd)
    return zscore
