---
title: "Flow Control: `if-else`"
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

{% include relblock.md target='dimension_validate.py' %}

That code checks if the argument is a `Number`, and if so, is it greater than zero.

## Task: Add Validation to Your Geometric Formulae

Add input validation to your `geom_formulae.py`.  Here is an **INCOMPLETE** example:

{% include relblock.md target='square_geom_with_validation.py' %}

Your code should validate in the following way:

 - if the arguments are anything other than a number, you should raise a `TypeError`
 - if the arguments are invalid because one or more are negative, you should raise a `ValueError`
 indicating which ones
 - if the arguments are invalid because they are incomplete, you should raise an `AttributeError`
 suggesting which additional arguments should be provided
 - if the arguments are invalid for other numerical reasons (*e.g.*, the three sides provided
 to a triangle-related method cannot form a triangle), then you should raise a `ValueError`
 explaining the problem.

Several people have code that already does some of this logic, but instead returns string
error messages.  Those people should replace their `return "error message"` with
the appropriate `raise XYZError("error message")`

In addition to this input validation, include or update your tests to verify that
your validation restrictions are working.
