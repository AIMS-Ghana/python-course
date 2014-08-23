def square_perimeter(side):
    """
    'square_perimeter' calculates a square's perimeter given a side length, e.g.:
    >>> square_perimeter(4)
    16

    :param side: the side length
    :return: the perimeter (same units as side length)
    """
    return 4*side


def square_area(side):
    return side*side

if __name__ == "__main__":
    sampleSide = 4
    print("area:", square_area(sampleSide),"perimeter:", square_perimeter(sampleSide))
