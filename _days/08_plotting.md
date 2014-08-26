---
title: Plotting
---

## How Do We Understand Results?

Sometimes, we want mathematical results in terms of a single numerical
outcome.  For example, the shape parameters or moments of a distribution.

However, often we may understand more from several points, or indeed a
continuous line or surface.

## Basic Turtle

{% include pyblock.md target="plot_ii.py" %}

## Basic Matplotlib

{% include pyblock.md target="plot_i.py" %}

aside: this is a preview of the capabilities of `numpy`.  You can just re-use
this application (namely `vectorize` and `linspace`) for your tasks now, and
we will cover `numpy` more thoroughly later.  However, if you want to read ahead,
feel free to start with [`vectorize`](http://docs.scipy.org/doc/numpy/reference/generated/numpy.vectorize.html)
and [`linspace`](http://docs.scipy.org/doc/numpy/reference/generated/numpy.linspace.html).

## Task: Draw Geometric Figures, Plot Properties

Using the shapes for which you implemented geometric formulae, create
functions that draw those shapes using turtles.

Then, create functions which will plot curves for their properties by varying one dimension.

For the twist points:

 - use your shape-turtle functions (possibly with some modification) to draw several
 shapes with the same area, but different perimeters.
 - for shapes or solids that have multiple dimensions, find a way to capture
 the effects of varying both

##
