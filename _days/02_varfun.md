---
title: "Variables, Functions"
prep: plotting
math: yes
---

## Mathematical Variables, Parameters, Functions, Equations, *etc*

What do each of the symbols in the following mean?

\begin{align}
f(\theta) = r\sin\theta + r\cos\theta
\end{align}

**DISCUSSION: WHAT CONCEPTS DO THESE IDEAS REPRESENT IN MATHEMATICS?**

## Translating that into Compu-speak

In programming, we have two kinds of language:

 - *reserved words*, also called *keywords* or sometimes syntax, the part the
 language defines
 - variables, functions, *etc* - the part we define

For many languages, this line can be blurry, much like the meaning of the \"+\"
in the equation we discussed earlier.  We will not get into those aspects of
Python during this course.

**DISCUSS: HOW DO THESE CONCEPTS LINK THE MATHEMATICAL ONES WE JUST REVIEWED?**

Example:

{% include pyblock.md target='square_geom.py' %}

## Task: Implement Geometric Formulae

Your assignment:

 - create a file in your local repository named `geom_formulae.py`
 - pick at least 10 other shapes or solids for geometric properties (*e.g.*,
   perimeter, area, volume, surface area)
 - implement those formulae as functions  and verify the results for dimensions
 that you can check with pen and paper
 - challenge: who can implement the most formulae?

Feedback will be out of 10 points, 2 points corresponds to passing.  Assignments
are turned in by pushing your work to your GitHub repository.

 - To get any points at all, you must earn these 2:
    * have at least ten formulae, 1 point
    * those formulae work, 1 point
 - you check a classmates work and they pass their assignment, 1 point
 - your script complies with PEP-8, 1 point
 - if all of your working formulae:
    * have informative names, 1 point
    * have informative argument names, 1 point
    * have documentation, 1 point
    * that documentation includes a demonstration case, 1 point
 - you have at least one property that can be calculated with different kinds of
 arguments, 1 point
 - you have at least one formula with 3 or more meaningful arguments, 1 point

Future assignments will be evaluated similarly: a few points for the absolute
minimum, a point for checking classmates work, more points for following good
coding practices, and then a point or two for a twist.

All assignments are turned in by (1) pushing your work to your github repository,
and (2) by emailing the pertinent files to in reply to the assignments email.
