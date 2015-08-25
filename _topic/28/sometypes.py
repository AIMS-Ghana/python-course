__author__ = 'cap10'

someint = 5
somedouble = 5.0
somestring = "a string"

print(type(someint), type(somedouble), type(somestring))

# but also

import turtle

ss = turtle.Screen()
tt = turtle.RawTurtle(ss)

print(type(ss), type(tt))