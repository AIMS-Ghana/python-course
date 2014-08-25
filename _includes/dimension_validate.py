from numbers import Number

def dimension_validate(dim):
    if isinstance(dim, Number):
        return dim >= 0
    else:
        return False


def dim_validate(dim):
    return isinstance(dim, Number) and dim >= 0

if __name__ == "__main__":
    print(dimension_validate(5))
    print(dimension_validate(-5))
    print(dimension_validate("string"))
    print(dimension_validate(0.2))
