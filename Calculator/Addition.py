def addition(a, b):
    a = float(a)
    b = float(b)
    c = a + b
    return c


def stats_addition(val1, val2, val3, val4, val5, val6, val7, val8, val9, val10):
    try:
        values = [val1, val2, val3, val4, val5, val6, val7, val8, val9, val10]
        values_sum = sum(values)
        return values_sum
    except TypeError:
        print("Cannot Input Text")








