from square_geom import *
from nose.tools import *

def test_square_area_int():
    assert square_area(1) == 1
    assert square_area(4) == 16
    s = 5
    assert square_area(s*2) == 4*square_area(s)


eps = 1e-6
def test_square_area_double():
    assert 25/4 - eps < square_area(2.5) < 25/4 + eps

@raises(TypeError)
def test_square_area_other():
    square_area("a string")

def test_square_perimeter_int():
    s = 5
    assert square_perimeter(s) == 20
    assert square_perimeter(4*s) == square_perimeter(s)*4


def test_fail_square_perimeter():
    assert square_perimeter(4) == 20
