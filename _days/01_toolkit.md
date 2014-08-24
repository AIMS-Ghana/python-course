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

Note that *brains* is plural.  The social aspect of programming is enormously enriching.
Like any discipline, the work can be done for ourselves; but programming is at
heart about expressing ideas.  A fair portion of the resulting software is shared
with others - someone else will run the program to enjoy its result - and most
any sophisticated project requires many minds of the life of the work.

## Python Console / Interactive Shell / REPL

**WHAT DOES REPL STAND FOR?  EXPLAIN THE CONCEPT.**

On a vintage macbook:

~~~
computername:python-course username$ python3  
Python 3.3.2 (v3.3.2:d047928ae3f6, May 13 2013, 13:52:24)
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.  
>>>
~~~

This interface can be used to do essentially anything Python.  But: there are
certain uses that are preferable to others.  Basically, code that is one to
a few lines:

{% highlight python %}
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

Start the PyCharm application.  There will be some initial use questions.  If
you want to have your screen look like mine, you should choose the `darcula`
theme.

We will make a few other changes in the settings, specifically in
[appearance](http://www.jetbrains.com/pycharm/webhelp/editor-appearance.html) and
[testing](http://www.jetbrains.com/pycharm/webhelp/python-integrated-tools.html).

You should create a project named `intro-python`; we will do our course work in
this directory.

Now create a new Python file (either via hotkeys ctrl-N, or by right clicking
the project and selecting \"new...\", or by using the dropdown menus) named
`hw` (the `.py` extension will be added automatically).

**WRITE CODE THAT CAUSES THE STRING `HELLO WORLD` TO APPEAR WHEN YOU RUN THE
SCRIPT**

**NEXT LAUNCH THE CODE FROM THE TERMINAL COMMAND PROMPT**

These two tasks are fundamentals you will repeat throughout the course:
creating a script and verifying that it works by running it.

## Git + GitHub

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

We will now turn the project directory you just created into a repository
and connect it to a remote repository.

**RECALLING THE STEPS FROM THE PREREADING, CONNECT A LOCAL GIT REPOSITORY
TO A REMOTE REPOSITORY ON GITHUB.**

We create a repository to provide history, a means to create drafts, a way to
share code, among other reasons.  We will demonstrate the first two with the
next tasks.

We will make a minor modification to our `hw` script, to narrow our ambitions:

**CHANGE YOUR SCRIPT TO SAY HELLO TO GHANA INSTEAD OF THE WHOLE WORLD.**

Now that we have made changes, we need to record our progress in the repository.

**RECALLING THE STEPS FROM THE PREREADING, COMMIT YOUR CHANGES AND THEN UPDATE
THE REMOTE REPOSITORY.**

**ONCE YOU HAVE UPDATED, LOCATE THE REPOSITORY IN YOUR GITHUB ACCOUNT AND REVIEW
THE COMMIT RECORDS.**

## PREP FOR NEXT SESSION

 - learn how to declare variables and functions in Python (hint: use Google, or
   consult a classmate, or a textbook)
