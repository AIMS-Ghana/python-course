__author__ = 'cap10'

def print_info(t):
    try:
        print("whole:",t)
        print('max:',max(t),
              'min:',min(t),
              'sum:',sum(t))
    except TypeError as err:
        print(err.args[0])
    finally:
        print()

aset = {1, 2, 3, 3}
print_info(aset)

import turtle

bset = {1, 'two', 3.0, turtle.Screen()}
print_info(bset)

## but also:

aset.add(5)
print_info(aset)

for thing in aset:
    print(thing)