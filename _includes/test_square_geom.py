from square_geom import *

def test_square_area():
    assert square_area(4) == 16


def test_square_perimeter():
    assert square_perimeter(4) == 16


def test_fail_square_perimeter():
    assert square_perimeter(5) == 20