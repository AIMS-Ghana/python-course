---
title: Flow Control with For and While
prep: objects
---

## Sequential Iteration with `for` loops

A `for` block iterates over the items in a collection, and executes for each of
those items.  Here are several examples:

{% include relblock.md target="for_i.py" %}

What does the last iteration correspond to?

## Searching Iteration with `while`

A `while` block loops as long as a condition is met.  It can simulate a `for` loop:

{% include relblock.md target="for_ii.py" %}

but more generally it is used for checking a more complicated conditional.  If
we wanted to calculate the Fibonacci sequence to a fixed approximation of $\phi$
rather than for a fixed number of steps:

{% include relblock.md target="while_i.py" %}

## Task: Implement the Secant Method

Basic requirement: provide a method that receives

 - a function,
 - two initial guesses for zeroes,
 - and a desired tolerance

and using those, applies the Secant method.

From here on, your assignments should always do appropriate input validation.

The twist points:
 - provide an alternative implementation that can use the derivative (another function argument), which is of
course the Newton-Rhapson Method.
 - have the program determine which approach to use based on the input to the same
 function

Your results will be evaluated based on a function `(x: Number) -> Number` we supply to your code.

## Task: Implement the Midpoint, Trapezoid, and Simpson\'s Methods

Basic requirement: provide methods that receive

 - a function (again, `(x: Number) -> Number`),
 - start and end points,
 - and a resolution,

and using those applies the appropriate integration method.

Remember: input validation!  Also, recall the `np.linspace` method we borrowed from
`numpy` earlier.

Twist points:

 - provide a method which receives the above info as well as a string
 \"midpoint\", \"trapezoid\", \"simpson\", and dispatches to the requested method
 - also be able to receive a series of points as an argument
 - provide a method that will plot the integral for a particular function and endpoints
 as a function of the resolution.

## Starting Script

This script skeleton may be a useful starting point:

{% include relblock.md target="skeleton_methods.py" %}
