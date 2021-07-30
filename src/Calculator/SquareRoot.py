def sqrt(a):
    a = float(a)
    if a >= 0:
        return round(float(a)**.5, 10)
    else:
        raise ValueError("Input is a not a non-negative integer!")
