---
title: Using a Program
warmup: true
hw: true
---

## HW Review

What did people have the most trouble figuring out? [ask random](#askrandom){:.random}

## Programming

Thing big: what was this homework about?

## Key Python Ideas

 - using the interpreter
 - writing a script, particularly with a "shebang" a/k/a `#!` line
 - using command line arguments
 - variables

## Advanced Version

Create a `hw3.py` in your homework directory, which behaves like:

{% highlight bash %}
{{ site.hwprompt }} ./hw3.py
hello World!
{{ site.hwprompt }} ./hw3.py Carl Des Ghana
hello Carl, Des, and Ghana!
{{ site.hwprompt }} ./hw3.py Some Other Names
hello Some, Other, and Names!
{% endhighlight %}

When you have completed this, add it to your repository.  You can't use the `turnin` script
for this, since it only updates existing files:

{% highlight bash %}
{{ site.hwprompt }} git status
...output about your repository
{{ site.hwprompt }} git add hw3.py
{{ site.hwprompt }} git commit -m "add hw3 to repo"
{{ site.hwprompt }} git push
{% endhighlight %}

The tool `git` is for doing *version control*.  This is very important for complicated
projects, so we will be using it as part of the course.  However, we won't go into
details, since it's a lot of extra work for this level of coding.

## Project Advice

The project assignments both entail programs run from the command line, that receive
arguments.  You should now know how to at least draft that part of the problem.