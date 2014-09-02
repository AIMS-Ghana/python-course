from dimension_validate import *

def square_perimeter(side : Number) -> Number:
    """
    Calculate perimeter of a square from side length.

    @param side: the side length
    @return: the perimeter (same units as side length)

    >>> square_perimeter(4)
    16
    """
    if (dim_validate(side)):
        return 4*side
    else:
        raise ValueError("side is less than 0: "+str(side))