import numpy as np
from math import sqrt, pi


x = np.linspace(-4*sqrt(3), 4*sqrt(3), 1000)
y = 1 / np.sqrt(2 * pi) * np.exp(-x ** 2 / 2)
gs = (1 - sum(y * (x[1] - x[0])))
print(gs)