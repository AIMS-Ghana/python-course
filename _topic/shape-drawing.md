---
title: Shape Drawing Project
---

## Project Overview

You will write a program that will draw shapes in various colors, sizes, and positions,
overlapping each other on a single plot.  This program should accept an
input csv with rows for each shape, and optionally a target output.

## Input Format

The input will be a csv file, with each row in this format (`f` means floating point number,
`r` means degrees [0,360)):

{% highlight text %}
(SQUARE|TRIANGLE|CIRCLE|RECTANGLE), (RED|ORANGE|YELLOW|GREEN|BLUE|PURPLE), r, f, f, f
{% endhighlight %}

The floating point numbers are (total area, x-origin, y-origin).  The RECTANGLE option means a golden rectangle, TRIANGLE means an equilateral triangle, and the origins provide relative position of the shape.  The angle is the rotation of the shape.

If an invalid input file is provided, the program should respond with useful input.

## Output Format

If no output file is provided, the program should draw the shapes for the user in realtime.

If an output file is provide, the program should save a png of the final picture.

## Example Usage

In summary, you program should run as:

{% highlight bash %}
python-course-homework username$ ./shape-drawing.py garbageinput.csv
Error: ... indicate what is wrong on the first line with an error ...
python-course-homework username$ ./shape-drawing.py
... same as next line ...
python-course-homework username$ ./shape-drawing.py -h
... useful info about usage ...
python-course-homework username$ ./shape-drawing.py input.csv
... real time animation of shape drawing ...
python-course-homework username$ ./shape-drawing.py input.csv output.png
python-course-homework username$ ls output.png
... finds plot you just made ...
{% endhighlight %}

## Process

As you make progress on this assignment, you should be committing updates to your
branch in the repository.

When you think you are ready, you should have committed all of your revisions and pushed
them to the repository.  Then email your TA indicating this project is ready for evaluation.

If you finish early, we can talk about extensions to the project.

On the last day of class, you should be prepared to demonstrate your project from the commandline.  You will probably want to create some input files to show different results (and your artistic skills).