---
title: Intro to `numpy`
math: yes
---

## First: Last Task

For the remainder of the course, you will be working on analyzing a system of
differential equations that forms the basis of a common family of models:
the *SIR* equations.

*SIR* stands for **S**usceptible-**I**nfectious-**R**ecovered (or sometimes
*R*emoved), and it is a basic *compartment model* for studying the spread of infection
in a population.  Each compartment is the amount of the population that corresponds
to the relevant state:

 - has never experienced the infection (**S**)
 - is currently sick and can spread the infection (**I**)
 - is now immune (**R**) due past exposure, vaccination, *etc*.

{% include sir.liquid %}

For the final project, we will be producing numerical analyses of this system.

## `numpy`

The `numpy` module provides a complete system for working with series of numbers,
particularly objects in linear algebra like matrices and vectors, but also more
generally.  The [tutorial](http://wiki.scipy.org/Tentative_NumPy_Tutorial) is
fairly complete.

We are going to start by revisiting our numerical equation work.

{% include relblock.md target="numpy_review.py" %}

Now we will look at some Project Euler problems, specifically [6](https://projecteuler.net/problem=6)
and [11](https://projecteuler.net/problem=11).

{% include relblock.md target="euler_06.py" %}

{% include relblock.md target="euler_11.py" %}

Finally, we should do some plotting.

{% include relblock.md target="numpyplotting.py" %}
