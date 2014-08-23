def dimension_validate(dim):
    if isinstance(dim, (int, float)):
        return dim > 0
    else:
        return False


if __name__ == "__main__":
    print(dimension_validate(5))
    print(dimension_validate(-5))
    print(dimension_validate("string"))
    print(dimension_validate(0.2))
