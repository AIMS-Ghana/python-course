import turtle


def draw_square(side):
    i = 0
    while (i < 4):
        turtle.forward(side)
        turtle.left(90)
        i = i+1
    turtle.done()


if __name__ == "__main__":
    draw_square(50)