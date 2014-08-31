---
title: "Flow Control I: `if-else`"
prep: errors
---

## Recall: Piece-wise defined Functions And Function Domains

**DISCUSS: WHAT ARE SOME EXAMPLES OF PIECEWISE DEFINED FUNCTIONS?**

**WHAT ARE SOME EXAMPLES OF FUNCTIONS WITH RESTRICTED DOMAINS?**

**BONUS: WHAT ABOUT MATHEMATICAL LOGIC?**

## Python for Piecewise Behavior: `if-elif-else`

In programming tasks, we often want conditional results.  If we have some
particular input, then we want a particular output.  This is more nuanced than
how we have been using functions so far: we saw different particular outputs for
different particular inputs calculating geometric properties.  But these results
are analogous to the associated continuous mathematical relations: there are no
discontinuous transitions in outcomes.

For these geometric formulae, many of you probably overlooked that there *should*
be some sharp transitions in behavior.  For example, consider what happens here:

{% highlight python %}
>>> square_area(-4)
16
{% endhighlight %}

**DISCUSS: WHAT ARE THE ISSUES WITH THAT RESULT? HOW WOULD WE WANT THEM TO BE RESOLVED?**

## `if` for Domain Restriction

In our geometry cases, we have fairly simple restrictions on domain: dimensions should
not be negative.

How would we express that?  Here is one possibility:

{% include pyblock.md target='dimension_validate.py' %}

That code checks if the argument is a `Number`, and if so, is it greater than zero.

## Task: Add Validation to Your Geometric Formulae

Using code like that in `dimension_validate.py`, add input validation to your
geometric functions.  Consider the example:

{% include pyblock.md target='square_geom_with_validation.py' %}

We will be talking more about the last bit, `raise ...`, in a later session.
For now, you should `raise ValueError("message")`, with an appropriate message
corresponding to what is wrong with the inputs.

## Task II: Project Euler

We will now also start on the [ProjectEuler.net](http://projecteuler.net/problems)
problems.  You will need to make an account, locate your friend key, and provide
that to me and the tutors via email.  By next Monday, solve at least 10 problems.
We will cover all the necessary syntax tools this week, but you will want to start
thinking about the algorithm to solve some of these problems prior to that.

WARNING: DO *NOT* PUT ANY CODE YOU USED TO SOLVE PROJECT EULER PROBLEMS IN YOUR
REPOSITORY.  WHEN SOLVING THE PROJECT EULER PROBLEMS, DO *NOT* SIMPLY SEARCH FOR
SOLUTIONS.
