---
title: Flow Control with For and While
warmup: true
hw: true
---
{% include startup.md %}

## Key Research Ideas

 - sequential vs conditional loops

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

## Advanced Version

We've done two basic loops, `for` loop for the mid-point method
and `while` loop for bisection root finding.  Now we'll implement another integrator (the Trapezoid Method in `trapeziod.py`) and another root finder (the Secant Method in `secant.py`).

Once you've done so, the following code (already in your homework directory) should work:

~~~
{{ site.hwprompt }} ./try_integrators2.py
...
{{ site.hwprompt }} ./try_roots2.py
...
~~~