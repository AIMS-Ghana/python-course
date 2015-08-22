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

def midpoint(f, a, b, n):
    deltaX = (b-a)/n
    start = a + deltaX/2
    end = b - deltaX/2
    mids = np.linspace(start, end, n)
    fs = f(mids)
    fsum = np.sum(fs)
    return deltaX*fsum


def trapezoid(f, a, b, n):
    deltaX = (b-a)/n
    points = np.linspace(a, b, n+1)
    fpoints = f(points)
    res = fpoints[0]+fpoints[-1]+2*np.sum(fpoints[1:-1])
    return res * deltaX/2


poly_coeffs = [1,2,3,5]

def f1(x):
    return x**3 + 2*x**2 + 3*x + 5


pf1 = np.poly1d(poly_coeffs)

a, b = 0, 10

n = 100

print(simpsons(f1,a,b,n))
print(midpoint(f1,a,b,n))
print(trapezoid(f1,a,b,n))

pfi = pf1.integ()
print(pfi(b)-pfi(a))