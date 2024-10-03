from math import e, fabs


def f(x):
    return x*(2+e**x+e**(-x))-2*e**(-x)

l, r = 0, 10
eps=1e-5
while l < r:
    mid = (l+r) / 2
    if fabs(f(mid) - 2) < eps:
        print('w:', mid)
        print('b:', -2*mid)
        break
    elif f(mid) < 2:
        l = mid
    else:
        r = mid