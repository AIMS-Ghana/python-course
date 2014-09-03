__author__ = 'cap10'

import turtle

class Square(object):
    """a class representation of square"""
    squares_created = 0
    def __init__(self, side_length:(int,float)):
        self.squares_created += 1
        self.side_length = side_length

    def __str__(self):
        return "Square, side length: "+str(self.side_length)

    def area(self):
        return self.side_length**2

    def perimeter(self):
        return self.side_length*4

    def draw(self):
        for i in range(0,4):
            turtle.forward(self.side_length)
            turtle.left(90)
        turtle.done()

sq = Square(50)
print(sq,sq.area(),sq.perimeter())
sq.draw()