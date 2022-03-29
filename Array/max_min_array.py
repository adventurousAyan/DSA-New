def getMinMax(a, n):

    min = float("inf")
    max = float("-inf")

    for val in a:
        if val > max:
            max = val
        if val < min:
            min = val
    return min, max


a = [3, 2, 1, 56, 10000, 167]
print(getMinMax(a, 6))
