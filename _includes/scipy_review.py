__author__ = 'cap10'

import numpy as np


def simpsons(f, a, b, n):
    deltaX = (b-a)/n
    points = np.linspace(a, b, n+1)
    fpoints = f(points)
    coeffs = np.zeros(n-1)
    coeffs[0::2] = 4
    coeffs[1::2] = 2
    # coeffs should be 4,2,4,...,2,4
    res = fpoints[0] + np.sum(coeffs*fpoints[1:-1]) + fpoints[-1]
    # res = fpoints[0] + 4*np.sum(fpoints[1:-1:2])
    # + 2*np.sum(fpoints[2:-1:2]) + fpoints[-1]
    return deltaX/3*res


def f1(x):
    return np.exp(x-1) - x**2

a, b = 0, 10
n = 10


print(simpsons(f1,a,b,n))
print(simpsons(f1,a,b,n*10))

from scipy.integrate import quad

print(quad(f1, a, b))

from scipy.optimize import root

print(root(f1,10))