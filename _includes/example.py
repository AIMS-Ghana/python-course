__author__ = 'cap10'

from obj_circle import Circle
from obj_square_ii import Square
from obj_rect import Rectangle

def calc_circle():
    radius = float(input("Please enter the radius: "))
    return Circle(radius)

def calc_square():
    sl = float(input("Please enter the side length: "))
    return Square(sl)

def calc_rectangle():
    sl = float(input("Please enter the length: "))
    sw = float(input("Please enter the width: "))
    return Rectangle(sl,sw)

options = { 'circle':calc_circle , 'square':calc_square, 'rectangle':calc_rectangle }

def print_options():
    print("options are:")
    for s in options.keys():
        print(" -", s)
    return input("select a shape or enter 'quit': ")


def interactive():
    print("welcome blah-blah")
    selection = print_options()
    while selection != 'quit':
        if selection in options.keys():
            try:
                print( options[selection]() )
            except (TypeError, ValueError) as err:
                    print(err.args[0])
        else:
            print("I don't understand", selection)
        selection = print_options()




if __name__ == "__main__":
    interactive()