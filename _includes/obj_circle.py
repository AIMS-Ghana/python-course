__author__ = 'cap10'

import turtle, math
from obj_square_ii import Shape

class Circle(Shape):
    """a class representation of square"""
    circles_created = 0
    def __init__(self, radius:(int,float)):
        super(Circle, self).__init__(radius=radius)
        self.circles_created += 1
        self.radius = radius
        self.area = math.pi * radius**2
        self.perimeter = 2*math.pi*radius

    def __str__(self):
        return super(Circle, self).__str__()+\
               "; radius: "+str(self.radius)

    def __cmp__(self, other):
        if not isinstance(other, Circle):
            raise TypeError
        else:
            return self.radius - other.radius

    def draw(self):
        turtle.circle(self.radius)
        turtle.done()


if __name__ == "__main__":
    c = Circle(50)
    print(c)
    c.draw()