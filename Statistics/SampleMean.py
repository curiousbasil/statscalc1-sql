def sample_mean(val1, val2, val3, val4, val5):
    try:
        mean_values = [val1, val2, val3, val4, val5]
        mean_float = [float(i) for i in mean_values]
        mean_length = len(mean_float)
        mean_sum = sum(mean_float)
        return mean_sum/mean_length
    except TypeError:
        print("Sample Mean is a Number. Cannot Input Text")


