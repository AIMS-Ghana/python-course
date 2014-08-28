---
title: Testing
prep: ifelse
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

## Unit Testing With `nose`, `doctest`

Consider tests of the previous example calculating geometric properties
for a square:

{% include pyblock.md target='test_square_geom.py' %}

What are the notable points?

 - new keyword `assert`
 - function definitions start with `test_`

We can run these tests by right-clicking our project directory and selecting
\"Run Nosetests\...\".  The `nose` module does unit testing using an approach
with simpler syntax that the built-in `unittest` module.

**QUERY: WHERE ELSE HAVE YOU SEEN TESTS ALREADY?**

The `doctest` functionality is another approach to testing.  It allows for tests
to be baked directly into your documentation.

## Task: Write Tests for Your Previous Geometric Functions

Basic requirement: for your previous work with geometric formulae, write tests
using both the `doctest` approach (which you may have already done) and the `nose`
approach.  Verify those tests work both via PyCharm and the terminal; your
submission should include a bash script that will run all your tests.

Twist points:

 - for each of your formulae, write tests that your method *should* handle but
 currently does not (*e.g.*, what happens when your function receives negative
 arguments? or strings?).  These tests should fail.
