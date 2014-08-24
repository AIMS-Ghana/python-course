def square_perimeter(side):
    """
    'square_perimeter' calculates a square's perimeter given a side length:
    >>> square_perimeter(4)
    16

    :param side: the side length
    :return: the perimeter (same units as side length)
    """
    return 4*side


def square_area(side):
    """
    'square_area' calculates a square's area given a side length:
    >>> square_area(4)
    16

    :param side: the side length
    :return: the area (units^2 from side)
    """
    return side*side

if __name__ == "__main__":
    sampleSide = 4
    print("area:",
          square_area(sampleSide),
          "perimeter:",
          square_perimeter(sampleSide))
