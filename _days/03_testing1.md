---
title: Testing
---

## Proof and Programming

Typically, the rules in programs are more complex than those in mathematical syntax.
There tends to be a lot more abstraction baked directly into the syntax of any particular
language than is contained in operators in math.

This means that proving the truth of some program statement is likewise more
involved.

Much of the power of mathematics comes from provability - that some statement,
properly applied, remains true in many different contexts.  Because such
proofs are not typically available for computer code, we need other approaches
to given us *confidence*, if not certainty, in the results of our computations.

Having tests associated with our code can provide some of that confidence.

## Unit Testing With Nose

Consider tests of the previous example calculating geometric properties
for a square:

{% highlight python %}
{% include test_square_geom.py %}
{% endhighlight %}

We can run these tests

## Task: Write Tests for Your Previous Geometric Functions

## PREP FOR NEXT SESSION

 - find and read documentation about `if-elif-else` syntax for Python (e.g., [this](http://www.java2s.com/Code/Python/Language-Basics/If.htm))
 - research input validation (e.g., [this](http://openbookproject.net/pybiblio/tips/wilson/validating.php))
