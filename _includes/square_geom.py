from numbers import Number

def square_perimeter(side : Number) -> Number:
    """
    Calculate perimeter of a square from side length.

    @param side: the side length
    @return: the perimeter (same units as side length)

    >>> square_perimeter(4)
    16
    """
    return 4*side


def square_area(side):
    """
    Calculate area of a square from side length.
    @param side: the side length
    @return: the area (units^2 from side)
    >>> square_area(4)
    16
    """
    return side*side

if __name__ == "__main__":
    sampleSide = 4
    print("area:",
          square_area(sampleSide),
          "perimeter:",
          square_perimeter(sampleSide))
