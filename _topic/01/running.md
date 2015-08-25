---
title: Using a Program
warmup: true
hw: true
---
{% include startup.md %}

## Key Python Ideas

 - using the interpreter (also, possibly pre-checking work in REPL, IDE)
 - writing a script, particularly with a "shebang" a/k/a `#!` line
 - using command line arguments
 - variables

## Advanced Version

Create a `hw3.py` in your homework directory, which behaves like:

{% highlight bash %}
{{ site.hwprompt }} ./hw3.py
hello World!
{{ site.hwprompt }} ./hw3.py Carl Des
hello Carl and Des!
{{ site.hwprompt }} ./hw3.py Carl Des Ghana
hello Carl, Des and Ghana!
{{ site.hwprompt }} ./hw3.py Some Other Names Too
hello Some, Other, Names and Too!
{% endhighlight %}

When you have completed this, add it to your repository.  You can't use the `turnin` script
for this, since it only updates existing files, so you'll need to add the file:

{% highlight bash %}
{{ site.hwprompt }} git status
...output about your repository
{{ site.hwprompt }} git add hw3.py
{{ site.hwprompt }} git commit -m "add hw3 to repo"
{{ site.hwprompt }} git push
{% endhighlight %}

The tool `git` is for doing *version control*.  This is very important for complicated
projects, so we will be using it as part of the course.  However, we won't go into
details very deeply, since it's a lot of extra work for this level of coding.  You can take
this opportunity to familiarize yourself with the tool, however.

## Project Advice

The project assignments both entail programs run from the command line and that receive
arguments.

For the SEIR model, formatted outputs (which we talked about as part of `hw3.py`) are also useful.

You should now know how to at least draft that part of the problem.  You can start on your code by creating
the appropriate files in your repository, and adding comments (or even actual code) that solves just this piece of the problem.  Later you can adjust that code as necessary, and integrate it with the rest of your solution.