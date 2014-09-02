---
title: "Flow Control: Errors"
prep: forwhile
---

## What are Errors?

Certainly, some of you have gotten less-than-perfect grades on work you have done
leading up to this.

What caused you to get less than perfect scores?  Probably some combination of:

 - you did everything \"right\", but had incomplete knowledge or logic
 - you had incorrect knowledge or logic
 - you ran out time trying to complete the work

Can errors be useful?

**DISCUSS: WHEN HAVE YOU FOUND ERRORS USEFUL?  WHAT MADE THOSE ERRORS USEFUL, DISTINCT
FROM THE ONES THAT WERE NOT?**

## Errors in Programs

By now, you have seen some errors in your programs.  On some occasions, the
dreaded red text in the console.  But you have probably also seen cases where
Python did not complain, yet the results were still wrong. Those of you that
tackled some of the more challenging aspects of the earlier assignments, for
example using default arguments to allow the same geometric calculate to be
accomplished several ways, probably found some cases where you *wanted* your
program to have an error.

Python, like many other languages, deals with errors via *Exceptions*.

Exceptions provide a way of categorizing what errors are.  Which exception occurs
corresponds to what message someone using the code sees from the interpreter when
an error occurs.

## Handling Errors

Python uses flow control syntax to indicate what should be done with errors:

{% include pyblock.md target="try_geom.py" %}

**THIS CODE IS ACTUALLY NOT HANDLING POSSIBLE ERRORS.  WHAT IS THE PROBLEM?  HOW
SHOULD WE FIX IT?**

## Task: Continue Work on Input Validation
