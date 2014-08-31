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
We will cover the `while` syntax in a later session, and it is not necessary to
use to complete this assignment, but if you would like to research ahead and use
it, you should.

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
functions that draw those shapes using turtles.  We will be adding plotting for
solids later, but if you wish to start now, [start here](http://matplotlib.org/mpl_toolkits/mplot3d/tutorial.html).

Also create functions which will plot curves for their properties by varying one dimension.

For the twist points:

 - use your shape-turtle functions (possibly with some modification) to draw a single
 plot with several different shapes of the same area.  Vary the color of those
 shapes according to their relative perimeters.
 - for shapes or solids that have multiple dimensions, find a way to capture
 the effects of varying both
 - for each of the shapes and solids, plot the trends for two properties (*e.g.*, area
   and perimeter, volume and surface area)

## Task II: Provide Student Info For Course Site

Some people had trouble with this pseudo-task last week.  To review:

 - fork the course repository
 - **add** a file in the `_students/2014-2015` directory that is `YOURGITHUBUSER.md`
 - put in that file the information present in the `_students/_template.txt` file.
 - do *not* rename or replace that file
 - **NEW**, you should add a picture of yourself to the repository in the `students`
 directory.  The easiest way to do this will be to pull the repository to your
 machine, add the picture, commit, and push the results.  You may find this approach
 easier for the earlier steps as well, though they can be completed on the GitHub
 site

For convenience, the template file is:

~~~ yaml
---
name: Your Full Name, the name you go by first
country: Your Home
gh: "Your GitHib Handle (no @)"
---

Overwrite this with whatever content you want on your page.  A short professional blurb,
some resume-like info, *etc* are good options.  Keep in mind this is publicly
published on the internet.

This region *may* contain [kramdown](http://kramdown.gettalong.org/syntax.html) formated content.
~~~
