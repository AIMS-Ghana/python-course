---
title: Toolkit
---

## Pen[cil], Paper, Brains

These will prove your most productive tools by far.  But how do you use them for
programming problems?

Often in the way you would use them for math problems - as a way to lay out
details, by scribbling pictures or random thoughts or steps in a solution.
Whatever works as a way to make your thoughts concrete, then engage with them.

During the course, we will try various options, but I recommend you try to adapt
whatever you have made work for you when solving complex math problems.

**DISCUSSION BREAK: BRIEFLY DESCRIBE HOW YOU WORKED THROUGH A PROBLEM WHICH, AT LEAST
INITIALLY, TOOK MANY STEPS.**

## Python Console / Interactive Shell / REPL

**WHAT DOES REPL STAND FOR?  EXPLAIN THE CONCEPT.**

On a vintage macbook:

{% highlight bash %}
computername:python-course username$ python3
Python 3.3.2 (v3.3.2:d047928ae3f6, May 13 2013, 13:52:24)
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
{% endhighlight %}

This interface can be used to do essentially anything Python.  But: there are
certain uses that are preferable to others.  Basically, code that is one to
a few lines:

{% highlight bash %}
>>> 2 + 3
5
>>> _ + 3
8
>>> _ + 3
11
>>> from numpy import *
>>> pi
3.141592653589793
>>>
{% endhighlight %}

*etc* - with what you know now, you can use it like a calculator.  As we encounter
more syntax, you will be able to expand your usage in the interpreter.  However,
the best uses will continue to be few line interactions.

**WHAT DOES THE UNDERSCORE (`_`) APPEAR TO BE DOING?**

## Python Scripts, Running, Writing in an IDE - Pycharm

When you need to be able to think about more than a few lines at a time, you
should be writing a script.  Moreover, when you need to perform some task several
times, you should be writing a script.  Since this is one of the main reasons to
use a computer (repeating identical tasks), we will primarily work in this mode.

We will start with the task that you should always perform when you are first
trying to learn a new language: create and run a program that will produce the
phrase `hello world` on an appropriate output device.

## Git - GitHub

When you are writing, being able to have drafts provides several benefits:

 - if you hang onto the drafts at various stages, you can refer back to these
 drafts to see old ideas, and the evolution of your thinking
 - you are free to experiment with worrying about the results, because they are
 \"just drafts\"
 - other people can see your work process, and thus have confidence in the product

These benefits have been recognized in software engineering for many years, and
there are several flavors of tools falling under the broad category of *version control*
which provide a drafting mechanism.

As part of the course, we will use one of those tools: `git`.
