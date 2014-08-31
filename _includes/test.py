__author__ = 'cap10'

"""Copyright (C) 2011 by ZenX2

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, or modify the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE."""

from turtle import *
import random

def cube(cam, box):
    box[2] = box[2] / 20
    width = 300.0 #dimensions of the "screen"
    height = 300.0
    vertices = []
    vertices.append([0.0, 0.0, 0.0]) #every vertex.
    vertices.append([0.0, 0.0, 1.0 * box[2]])
    vertices.append([0.0, 1.0 * box[1], 0.0])
    vertices.append([0.0, 1.0 * box[1], 1.0 * box[2]])
    vertices.append([1.0 * box[0], 0.0, 0.0])
    vertices.append([1.0 * box[0], 0.0, 1.0 * box[2]])
    vertices.append([1.0 * box[0], 1.0 * box[1], 0.0])
    vertices.append([1.0 * box[0], 1.0 * box[1], 1.0 * box[2]])
    newverts = []
    for i in range(len(vertices)):
        vert = vertices[i]
        z = vert[2] + 1
        F = z - cam[2]
        """if (z == 0):
           z = 1 #uuuuuhh"""
        x = ((vert[0] - cam[0]) * (F / z)) + cam[0] + 1
        y = ((vert[1] - cam[1]) * (F / z)) + cam[1] + 1
        newverts.append([x, y])
    """for i in range(len(newverts)):
       #pu()
       goto(newverts[i])
       #pd()
       #dot(3)
       "=""rt(90)
       fd(20)
       rt(-90)
       fd(20)"=""
       print(i, newverts[i])"""
    pu()
    goto(newverts[0]) #manuel labor
    pd()
    #goto(newverts[])
    goto(newverts[4])
    goto(newverts[6])
    goto(newverts[2])
    goto(newverts[0])
    pu()
    goto(newverts[1])
    pd()
    goto(newverts[3])
    goto(newverts[7])
    goto(newverts[5])
    goto(newverts[1])
    goto(newverts[0])
    pu()
    goto(newverts[5])
    pd()
    goto(newverts[4])
    pu()
    goto(newverts[3])
    pd()
    goto(newverts[2])
    pu()
    goto(newverts[7])
    pd()
    goto(newverts[6])

#main
speed(0)

camera = [-5, -5, 10] #x,y,z

def moveright():
    camera[0] = camera[0] + 1

def moveleft():
    camera[0] = camera[0] - 1

def moveforward():
    camera[2] = camera[2] + .5

def moveback():
    camera[2] = camera[2] - .5

while (True):
    listen()
    onkey(moveright, "d")
    onkey(moveleft, "a")
    onkey(moveforward, "w")
    onkey(moveback, "s")
    boxinfo = [10.0, 10.0, 10.0] #width, height, depth; does not really make a cube
    cube(camera, boxinfo)
    clear()

done()