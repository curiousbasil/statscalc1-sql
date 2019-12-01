def mean(val1, val2, val3, val4, val5, val6, val7, val8, val9, val10):
    try:
        mean_values = [val1, val2, val3, val4, val5, val6, val7, val8, val9, val10]
        mean_float = [float(i) for i in mean_values]
        mean_length = len(mean_float)
        mean_sum = sum(mean_float)
        return mean_sum/mean_length
    except TypeError:
        print("Mean is a Number. Cannot Input Text")


