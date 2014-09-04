---
title: Objects
prep: lists
---

## Numbers *vs*. ?

Many of us learn mathematics as a sort of [physics of bottlecaps](http://www.cryptonomicon.com/main.html):
that the rules are about numbers, and that anything we figure out from maths
could ultimately be turned into a physical observation process,
such as counting bottle caps, or measuring lengths, masses, *etc*.

I am quite fond of this perspective, as it is implicitly reminds
us how to practice science via mathematical story-telling.

I am equally fond, however, of the notion of mathematics as being about
describing classes of things with certain shared features and operations, and
then being able to reason about the behaviors of those things without
reference to material things.

## Objects

You have worked with several types in Python so far:

{% include pyblock.md target="sometypes.py" %}

Integers and floating point numbers and character strings are probably familiar,
at least what the are, if perhaps not as a programming concept.

But what are those things associated with `turtle` plotting?  They are custom objects.

Revisiting our previous example shape:

{% include pyblock.md target="obj_square_i.py" %}

Here we have gathered the properties of a particular square in one place and
provided a uniform way to ask about them, and also to draw this particular
square.

However, we can do even more:

{% include pyblock.md target="obj_square_ii.py" %}

Here, we have create `Square` as a subclass of `Shape` and deferred certain
aspects to `Shape`, like input validation and building up the string representation.
If also make, say, a `Triangle` class from `Shape`, then the same input validation
will come along for free.

## Task: Convert Your Shape and Solid Work Into Objects

For the shapes and solids you have coded formulae for, make those into classes
that provide the area and perimeter (shapes) or surface area and volume (solids).

These classes should also provide the same methods as the example `Square`.  You
may extend the example class `Shape`  as your base class and use its input validation,
but be sure to appropriately credit the author.  You will still need to do input
validation, but you can consider all the inputs checked as positive numbers (if provided)
after the call to `super(\...)`.

For the twist points, argue what other methods should reasonably belong to
`Shape`s or `Solid`s.  Can they be implemented generically, *i.e.* on the abstract `Shape` and `Solid` classes,
or would they have to be implemented in specific types?
