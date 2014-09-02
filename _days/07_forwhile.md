---
title: "Flow Control: `for`, `while`"
prep: objects
math: yes
---

## Recall: Matrix Calculations, $\sum$ and $\prod$ Operators

## Sequential Iteration with `for` loops

## Accumulation with `for` loops

## Recall: Numerical Root Finding Methods

## Searching Iteration with `while`

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

Your results will be evaluated based on an `func(x: Number)` we supply to your code.

## Task: Implement the Midpoint, Trapezoid, and Simpson\'s Methods

Basic requirement: provide methods that receive

 - a function,
 - start and end points,
 - and a resolution,

and using those applies the appropriate integration method.

Remember: input validation!

Twist points:

 - provide a method which receives the above info as well as a string
 \"midpoint\", \"trapezoid\", \"simpson\", and dispatches to the requested method
 - also be able to receive a series of points as an argument
 - provide a method that will plot the integral for a particular function and endpoints
 as a function of the resolution.
