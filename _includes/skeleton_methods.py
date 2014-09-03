__author__ = 'cap10'

from math import sin, pi

def secant_method(f:callable,
                  guess0:(int,float), guess1:(int,float),
                  err : float) -> float:
    # assorted input validation
    x0, x1 = guess0, guess1
    condition = True # needs to be the actual condition of concern
    while condition:
        pass # update x0, x1, condition
    return x1

def midpoint_method(f:callable,
                    start:(int,float), end:(int,float),
                    intervals : int) -> float:
    # assorted input validation
    S = 0
    for i in range(0,intervals):
        # update S
        pass
    return S

# same for trapezoid, simpson's methods

def test_secant_method():
    err = 1-6
    assert pi-err < secant_method(sin, pi/2, 3*pi/2, err) < pi+err

def test_midpoint_method():
    # for high interval counts, the integrals should be roughly zero
    intervals = 100
    err = 1e-3
    assert 0-err < midpoint_method(sin, 0, 2*pi, intervals) < 0+err

# repeat tests for trapezoid, simpson's