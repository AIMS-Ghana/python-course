__author__ = 'cap10'

from square_geom_with_validation import *

def square_try(n=0):
    try: # steps you think might produce an error
        s = float(input("Provide a square side:"))
    except ValueError as err: # how you want to handle that error
        print("You did not enter a number, try again. Error:", err)
        square_try(n+1)
    else: # what to do if there was no error
        print("Square perimeter is:", square_perimeter(s))
    finally: # what to always do, errors or not
        print("exiting attempt",n+1)

if __name__ == "__main__":
    square_try()