__author__ = 'cap10'

import turtle

class Square(object):
    """a class representation of square"""
    squares_created = 0
    def __init__(self, side_length:(int,float)):
        self.squares_created += 1
        self.side_length = side_length
        self.area = self.side_length**2
        self.perimeter = self.side_length*4

    def __str__(self):
        return "Square, side length: "+str(self.side_length)

    def __cmp__(self, other):
        if not isinstance(other, Square):
            raise TypeError
        else:
            return self.side_length - other.side_length

    def draw(self):
        for i in range(0,4):
            turtle.forward(self.side_length)
            turtle.left(90)
        turtle.done()

sq = Square(50)

import math
print(math.sin)
print(sq,sq.area,sq.perimeter)
sq.draw()