---
title: Variables and Functions
warmup: true
hw: true
---

## HW Review

What did people have the most trouble figuring out? {% include random.md %}

## Programming

Thing big: what was this homework about? {% include random.md %}

## Key Python Ideas

 - old: using the interpreter, writing a script, using command line arguments and variables
 - defining functions
 - `if __name__ == "__main__"` paradigm

## Advanced Version

Create a `shapes.py` in your homework directory, which behaves like:

{% highlight bash %}
{{ site.hwprompt }} ./shapes.py
Error: no input
{{ site.hwprompt }} ./shapes.py TRIANGLE 1
equilateral triangle, area 1, sides: ...
{{ site.hwprompt }} ./shapes.py SQUARE 1
square, area 1, sides: ...
{{ site.hwprompt }} ./shapes.py CIRCLE 1
circle, area 1, sides: ...
{% endhighlight %}

When you have completed this, add it to your repository.

## Project Advice

The shape drawing project requires similar capabilities to the extended version of the homework.
