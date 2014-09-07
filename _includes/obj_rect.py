__author__ = 'cap10'

import turtle, math
from obj_square_ii import Shape

class Rectangle(Shape):
    """a class representation of square"""
    rectangles_created = 0
    def __init__(self, length:(int,float), width:(int,float)):
        super(Rectangle, self).__init__(length=length, width=width)
        self.rectangles_created += 1
        self.length, self.width = length, width
        self.area = length * width
        self.perimeter = 2*(length + width)

    def __str__(self):
        return super(Rectangle, self).__str__()+\
            "; length: "+str(self.length)+\
            "; width: "+str(self.width)

    def __cmp__(self, other):
        if not isinstance(other, Rectangle):
            raise TypeError
        else:
            return self.area - other.area

    def draw(self):
        for i in range(0,2):
            turtle.forward(self.length)
            turtle.left(90)
            turtle.forward(self.width)
            turtle.left(90)
        turtle.done()


if __name__ == "__main__":
    c = Rectangle(50,10)
    print(c)
    c.draw()