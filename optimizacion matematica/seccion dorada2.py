import math

phi = (1 + math.sqrt(5)) / 2
resphi = 2 - phi
def mss(f, a, b, tau=1e-5):
    c = a + (b-a) * resphi
    d = b - (b-a) * resphi
    fc = f(c)
    fd = f(d)
    while abs(b - a) > tau * (abs(c) + abs(d)):
        if fc < fd:
            b = d
            d = c
            c = a + (b-a) * resphi
            fd = fc
            fc = f(c)
        else:
            a = c
            c = d
            d = b - (b-a) * resphi
            fc = fd
            fd = f(d)
    return (a + b) / 2
