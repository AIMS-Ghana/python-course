---
title: Toolkit
---

## Pen[cil], Paper, Brains

These will prove your most productive tools by far.  But how do you use them for
programming problems?

Often in the way you would use them for math problems - as a way to lay out
details, by scribbling pictures or random thoughts or steps in a solution.  As
a way to make your thoughts concrete, then engage with them.

## Python Console / Interactive Shell / REPL

On a vintage macbook:

{% highlight bash %}
computername:python-course username$ python3.3
Python 3.3.2 (v3.3.2:d047928ae3f6, May 13 2013, 13:52:24)
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
{% endhighlight %}

This interface can be used to do essentially anything Python.  But: there are
certain uses that are preferable to others.  Basically, anything that is one to
few line use:

{% highlight bash %}
>>> 2 + 3
5
>>> _ + 3
8
>>> from numpy import *
>>> pi
3.141592653589793
>>>
{% endhighlight %}

*etc* - with what you know now, you can use it like a calculator.  As we encounter
more syntax, you will be able to expand your usage in the interpreter.  However,
the best uses will continue to be few line interactions.

## Python Scripts, Running, Writing in an IDE - Pycharm

When you need to be able to think about more than a few lines at a time, you
should be writing a script.

## Git - GitHub

When you are writing, being able to have drafts provides several benefits:

 - if you hang onto the drafts at various stages, you can refer back to these
 drafts to see old ideas, and the evolution of your thinking
 - you are free to experiment with worrying about the results, because they are
 \"just drafts\"
