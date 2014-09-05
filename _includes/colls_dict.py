__author__ = 'cap10'

def print_info(t):
    try:
        print("whole:",t)
        print('max key:',max(t.keys()),
              'max value:',max(t.values()))
    except TypeError as err:
        print(err.args[0])
    finally:
        print()

adict = {'one':1, 'two':2, 'three':3, 'four':3}
print_info(adict)

import turtle

bdict = {'one':1, 'two':'two', 3:3.0, 4.0:turtle.Screen()}
print_info(bdict)

## but also:

adict.update({'one':2})
print_info(adict)

for thing in adict:
    print(thing)

for key, val in adict.items():
    print(key,val)