---
title: Intro to `scipy`
---

## Remember! SIR Task

As we go over the capabilities `scipy` provides, particularly the options for
parameter fitting, think about what you want to do with the **SIR** model.

## What is `scipy` good for?

We saw that `numpy` provides simplification for work with numerical data, by
creating a simpler syntax for manipulation of vector and matrix data (and really
arbitrary tensor data, but we did not get into that aspect).  `numpy` also provides
some basic functions (*e.g.*, versions of the basic math functions that will work
with `nparray`s), basic numerical tools (*e.g.*, random number generation), and
some particular functions (*e.g.*, power series / polynomials).

That is quite a bit, but it does not cover many of ways in which we want to *use*
those things: namely representing equations and solving them.

Yesterday, we reviewed re-implementing some numerical integration techniques.  These
techniques were invented (or discovered, depending on your philosophy of mathematics)
several hundred years ago ([Simpson](http://en.wikipedia.org/wiki/Thomas_Simpson)
was an Englishman living in the 1700s, and he just popularized a method that had
been around for more than a century).

Unsurprisingly, there have been some advances since the advent of computers.  However,
most of these algorithms are quite sophisticated, and generally we are more interested
in their application than the particular details of implementing them.

The `scipy` module provides these methods in a packaged way.  We can revisit
our numerical integration and root finding activities using the `scipy` capabilities:

{% include relblock.md target="scipy_review.py" %}

Additionally, like `numpy` defines power series / polynomials, `scipy` also defines
special classes of functions.  These are the solutions to particular integro-differential
equations, such as Bessel functions.  We will not go over these, but they are
likely to come up in your later classes, so you might want to look into them now.

## Applying `scipy` to SIR model

Recall

{% include sir.liquid %}

We can represent these relationships in a straightforward computational way,
after noting \\(\dot{N}=0\\) in our particular specification:

{% include relblock.md target="SIR.py" %}

It is as simple as that to get the dynamics from a particular initial condition
and parameter combination.

Let us consider another typical question for the SIR model: what is the equilibrium
condition?  This is essentially a root-finding problem for multiple variables.

{% include relblock.md target="scipy_review_eq.py" %}
