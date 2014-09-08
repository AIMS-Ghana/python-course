__author__ = 'cap10'

import numpy as np


def simpsons(*args):
    pass


def midpoint(*args):
    pass


def trapezoid(*args):
    pass


poly_coeffs = [2,3,5]

def f1(x):
    pass


pf1 = np.poly1d([])

a, b = 0, 10

n = 100

print(simpsons(f1,a,b,n))
print(midpoint(f1,a,b,n))
print(trapezoid(f1,a,b,n))

pfi = pf1.integ()
print(pfi(b)-pfi(a))