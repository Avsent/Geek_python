def lev(a, b):
    return 1 / a ** (abs(b))
print(lev(2, -2))


def lev(a, b):
    mult = 1
    for i in range(abs(b)):
        mult = mult * a
    return 1 / mult
print(lev(2, -4))
