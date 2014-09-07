__author__ = 'cap10'

from obj_square_ii import Square
from obj_circle import Circle
from obj_rect import Rectangle

start_message = "Welcome to shape calculator."
quit_key = 'quit'
return_key = 'return'
reserved_words = { quit_key, return_key }

constructors = { 'square':Square, 'circle':Circle, 'rectangle':Rectangle }
arg_check = { 'square':['side_length'],
              'circle':['radius'],
              'rectangle':['length','width'] }


def shape_menu():
    print("please select a shape from the following menu, or enter 'quit':")
    for s in constructors:
        print(" -",s)
    return input("selection: ")


def check_par(par):
    res = float(par)
    if res < 0: raise ValueError(str(res)+" < 0")
    return res


def parameter_menu(plist):
    res = ()
    i = 0
    while res not in reserved_words and i < len(plist):
        par = input("input "+plist[i]+" (or '"+quit_key+"', '"+return_key+"'): ")
        if par not in reserved_words:
            try:
                formpar = check_par(par)
            except ValueError as err:
                print(plist[i],err.args[0],sep=": ")
            else:
                res = res + (formpar,)
                i += 1
        else:
            res = par
    return res


def interactive():
    print(start_message)
    shape = shape_menu()
    while shape != quit_key:
        if shape not in constructors.keys():
            print("did not understand shape '",str(shape),"'",sep="")
            shape = shape_menu()
        else:
            params = parameter_menu(arg_check[shape])
            if params not in reserved_words:
                made_shape = constructors[shape](*params)
                print(made_shape)
                print()
                shape = shape_menu()
            elif params == return_key:
                shape = shape_menu()
            else:
                shape = params

import csv

def fileparse(filename):
    with open(filename,'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ')
        for row in reader:
            if len(row) == 0:
                print("EMPTY ROW")
            else:
                which = row[0]
                params = row[1:]
                try:
                    con = constructors[which]
                    formparams = [check_par(x) for x in params]
                    shape = con(*formparams)
                except KeyError as err:
                    print("did not understand shape", which)
                except ValueError as err:
                    print(which,": ",err.args[0],sep="")
                except TypeError as err:
                    print(which,": ",err.args[0],sep="")
                else:
                    print(shape)

import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="process shapes data.", )
    parser.add_argument('-f', nargs=1, help="launch in file mode, must provide a file name", type=str)
    parser.add_argument('-i', action="store_const", const=True, help="launch in interactive mode")
    args = parser.parse_args()

    if not args.i and args.f:
        file = args.f[0]
        fileparse(file)
    elif args.i:
        interactive()
    else:
        parser.parse_args(['-h'])