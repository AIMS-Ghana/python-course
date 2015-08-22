__author__ = 'cap10'

def print_info(t):
    try:
        print("whole:",t)
        print("piece:",t[0])
        print("slice:",t[0:2])
        print('max:',max(t),
              'min:',min(t),
              'sum:',sum(t))
    except TypeError as err:
        print(err.args[0])

atuple = (1, 2, 3, 3)
print_info(atuple)

import turtle

btuple = (1, 'two', 3.0, turtle.Screen())
print_info(btuple)