---
title: Plotting
warmup: true
---

## HW Review

What did people have the most trouble figuring out?

## Programming

Thing big: what was this homework about?

## Key Research Ideas

 - plan to visualize results

## Key Python Ideas

 - old: defining functions
 - functions as inputs to functions
 - plotting libraries

## How Do We Understand Mathematical Results?

Sometimes, we want mathematical results in terms of a single numerical
outcome.  For example, the shape parameters or moments of a distribution.

However, often we may understand more from several points, or indeed a
continuous line or surface.

## Basic Turtle

Python has a basic library for drawing lines called `turtle`:

{% include relblock.md target="plot_ii.py" %}

You can direct turtles to move about and draw lines as they do so.  There are
more ways to direct the turtle, so feel free to consult the detailed documentation.
We will cover the `while` syntax in a later session, and it is not necessary to
use to complete this assignment, but if you would like to research ahead and use
it, you should.

## Basic Matplotlib

We will also be using a mathematical plotting library `matplotlib`, which has
capabilities appropriate to creating visualizations of scientific and
mathematical results.

{% include relblock.md target="plot_i.py" %}

You can basically create series of numbers (`S`, `A`, and `P` in this case), then
plot lines using those points as the reference.  There are several ways to change
the details of the lines (color, line type) and to annotate the plot (axis labels,
legends).

aside: this code has a preview of the capabilities of `numpy`.  You can just re-use
this syntax (namely `vectorize` and `linspace` to make your functions able to receive vector inputs) for your tasks now, and
we will cover `numpy` more thoroughly later.  However, if you want to read ahead,
feel free to start with [`vectorize`](http://docs.scipy.org/doc/numpy/reference/generated/numpy.vectorize.html)
and [`linspace`](http://docs.scipy.org/doc/numpy/reference/generated/numpy.linspace.html).