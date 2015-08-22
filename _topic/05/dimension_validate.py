from numbers import Number

def dim_validate(dim):
    """
    Test if dim is a Number and is >= 0.

    >>> dim_validate(5)
    True

    >>> dim_validate(-5)
    False

    >>> dim_validate("a string")
    False
    """
    return isinstance(dim, Number) and dim >= 0