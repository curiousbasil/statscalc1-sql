def median(val1, val2, val3, val4, val5, val6, val7, val8, val9):
    try:
        median_values = [val1, val2, val3, val4, val5, val6, val7, val8, val9]
        median_float = [float(i) for i in median_values]
        median_length = len(median_float)
        median_float.sort()
        if median_length % 2 == 0:
            median_index_1 = median_float[int(median_length // 2)]
            median_index_2 = median_float[int(((median_length // 2) - 1))]
            median3 = ((median_index_1 + median_index_2) // 2)
        else:
            median3 = median_float[int((median_length // 2))]
        return median3
    except TypeError:
        print("Median is a Number . Cannot Input Text")

