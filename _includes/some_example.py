__author__ = 'cap10'


def test_powmethod():
    assert powmethod(2.,2.) == powmethod(2,2)
    assert powmethod(3,3) == 27


def powmethod(a,b):
    """
    calculates a^b
    >>> powmethod(2.,2.)
    4.0
    """
    return a**b

def intpowmethod(a,b):
    """
    calculates a^b for b int only
    >>> intpowmethod(2,2)
    10
    """
    res = 1
    for i in range(b):
        res *= a
    return res


def badcode():
    """
    asdfasdfasdf
    """
    return "no error"


def ifwhileq():
    """
    does if-while order matter?
    """
    test_q = True
    while test_q:
        if test_q:
            test_q = False
        else:
            print("some other thing?")


import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="an argument parse example")
    parser.add_argument('-a', nargs=1, help="an example argument")


    args = parser.parse_args()
    print(args)
    pass