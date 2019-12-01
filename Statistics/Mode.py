from collections import Counter


def mode(val1, val2, val3, val4, val5, val6, val7, val8, val9, val10):
    try:
        mode_values = [val1, val2, val3, val4, val5, val6, val7, val8, val9, val10]
        mode_float = [float(i) for i in mode_values]
        mode_length = len(mode_float)
        count = Counter(mode_float)
        mode_result = dict(count)
        mode_calc = [c for c, m in mode_result.items() if m == max(list(count.values()))]
        if len(mode_calc) == mode_length:
            mode_result = "No mode found"
        else:
            mode_result = mode_calc[0]
        return mode_result
    except TypeError:
        print("Modeis a Number . Cannot Input Text")
