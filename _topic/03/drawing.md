---
title: Drawing
warmup: true
---
{% include startup.md %}

## Key Research Ideas

 - plan to visualize results

## Key Python Ideas

 - old: defining functions
 - functions as inputs to functions
 - plotting libraries

## Drawing vs. Plotting

There are two main tasks in visualization, which I will refer to as drawing and plotting.

In plotting, the scale and exact line positions are precise: ideally, you can determine exact numbers by reading off the lines with reference to the scales.  You can use the `numpy` plotting library by importing `pylab`.  We will be addressing plots later, when we learn about `numpy` and `scipy`.

In drawing, the scale and lines are aesthetic rather than precise.  It's still important to get them "right",
but right is subjective - the goal with drawing is to illustrate, rather than exact representation.  Python has a basic library for drawing called `turtle`.

## Advanced Version

We are going to modify your drawings to:

 1. make the shapes filled instead of lines
 2. take arguments for the fill color, but fill with black if no color is provided
 3. draw the figures on the same diagram, if requested

After you have modified your code, the `render_shapes2.py` script should produce a series of nested shapes in different colors, but your code **SHOULD CONTINUE TO WORK FOR THE ORIGINAL HOMEWORK**.  The one difference is that the shapes should be filled (if they weren't before).

## Project Advice

This is more capability that you need to complete one of the projects.  We also covered thinking about how to extend your existing work, and how to build that work in a way that can be extended.  You will need to do a bit more extension on your own for the project.