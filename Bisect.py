def sqrt(x):
    a = 0
    b = x

    while True:
        c = (a + b)/2
        Fc = c**2 - x

        if abs(Fc) < 0.000001:
            return c
        elif Fc < 0:
            a = c
        else:
            b = c
