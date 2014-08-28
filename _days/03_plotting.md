---
title: Plotting
prep: testing
---

## How Do We Understand Mathematical Results?

Sometimes, we want mathematical results in terms of a single numerical
outcome.  For example, the shape parameters or moments of a distribution.

However, often we may understand more from several points, or indeed a
continuous line or surface.

## Basic Turtle

Python has a basic library for drawing lines called `turtle`:

{% include pyblock.md target="plot_ii.py" %}

You can direct turtles to move about and draw lines as they do so.  There are
more ways to direct the turtle, so feel free to consult the detailed documentation.

## Basic Matplotlib

We will also be using a mathematical plotting library `matplotlib`, which has
capabilities appropriate to creating visualizations of scientific and
mathematical results.

{% include pyblock.md target="plot_i.py" %}

You can basically create series of numbers (`S`, `A`, and `P` in this case), then
plot lines using those points as the reference.  There are several ways to change
the details of the lines (color, line type) and to annotate the plot (axis labels,
legends).

aside: this code has a preview of the capabilities of `numpy`.  You can just re-use
this syntax (namely `vectorize` and `linspace` to make your functions able to receive vector inputs) for your tasks now, and
we will cover `numpy` more thoroughly later.  However, if you want to read ahead,
feel free to start with [`vectorize`](http://docs.scipy.org/doc/numpy/reference/generated/numpy.vectorize.html)
and [`linspace`](http://docs.scipy.org/doc/numpy/reference/generated/numpy.linspace.html).

## Task: Draw Geometric Figures, Plot Properties

Using the shapes for which you implemented geometric formulae, create
functions that draw those shapes using turtles.

Also create functions which will plot curves for their properties by varying one dimension.

For the twist points:

 - use your shape-turtle functions (possibly with some modification) to draw a single
 plot with several different shapes of the same area.  Vary the color of those
 shapes according to their relative perimeters.
 - for shapes or solids that have multiple dimensions, find a way to capture
 the effects of varying both
