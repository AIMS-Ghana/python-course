---
title: Intro to `numpy` and `scipy`
hw: true
warmup: true
---
{% include startup.md %}

## Key Research and Programming Idea

 - use already programmed modules, especially when they have a large community supporting, finding bugs, *etc*.
 - most research work involves complex integro-differential models, so know the appropriate libraries for this work

## `numpy`

The `numpy` library provides a variety of methods for creating and working with array-structured
data, particularly numerical data.  It also has some limited numerical methods.

{% include relblock.md target="numpy_review.py" %}

## `scipy`

The `scipy` library provides several tools for numerical methods - differentiation,
integration, special functions, *etc*.  These are designed to work with `numpy` structures.

{% include relblock.md target="SIR.py" %}

## Advanced Work

Add 5 functions to a `fun_plots2.py` file, then examine these with you `make_fun_plots.py` script.