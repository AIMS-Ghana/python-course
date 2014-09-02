from numbers import Number

## python varargs keyword arguments

## TODO what sort of error to raise?

def dim_validate(*args, **kwargs):
    result = True
    for arg in args:
        result = result and (
            isinstance(arg, Number) and arg >= 0
        )
    for key in kwargs:
        result = result and (
            isinstance(kwargs[key], Number) and kwargs[key] >= 0
        )
    return result


def test_one_correct_arg():
    assert dim_validate(1) == True


def test_multiple_correct_args():
    assert dim_validate(1, 2) == True


def test_one_correct_named_arg():
    assert dim_validate(one=1) == True


def test_multiple_correct_named_args():
    assert dim_validate(one=1, two=2) == True


def test_one_bad_arg_type():
    assert dim_validate("a string") == False


def test_multiple_bad_args_type():
    assert dim_validate("a string", "b string") == False


def test_single_bad_named_arg_type():
    assert dim_validate(one="a string") == False


def test_multiple_bad_named_arg_type():
    assert dim_validate(one="a string", two="b string") == False


def test_single_bad_arg_val():
    assert dim_validate(-1) == False


def test_multiple_bad_arg_val():
    assert dim_validate(-1, -2) == False


def test_single_bad_named_arg_val():
    assert dim_validate(one= -1) == False


def test_multiple_bad_named_arg_val():
    assert dim_validate(one= -1, two= -2) == False