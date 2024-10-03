from scipy.stats import poisson
import numpy as np


def f(x):
    return 1 / np.sqrt(2 * np.pi) * np.exp(-x ** 2 / 2)


x = np.linspace(-5 / 3, 5 / 3, 5000)
y = f(x)
gs = (1 - sum(y * (x[1] - x[0]))) / 2
print('Gaussian Distribution:', gs)

ps = 1 - sum(poisson.pmf(i, 900) for i in range(1, 951))
print('Poisson Distribution:', ps)