---
title: Variables and Functions
warmup: true
hw: true
---
{% include startup.md %}

## Key Python Ideas

 - old: using the interpreter, writing a script, using command line arguments and variables
 - defining functions
 - `import`ing from your own code
 - `if __name__ == "__main__"` paradigm

## Key Research Ideas

 - figure out what the pieces of your problem are
 - once you have good pieces, your can assemble them into more complicated analyses

## Advanced Version

Create a `shapes.py` in your homework directory, which should figure out side lengths from areas of CIRCLEs, SQUAREs, and equilateral TRIANGLEs, which behaves like:

{% highlight bash %}
{{ site.hwprompt }} ./shapes.py
... error indicating no input...
{{ site.hwprompt }} ./shapes.py OCTAGON 1.5
... error indicating unknown shape...
{{ site.hwprompt }} ./shapes.py TRIANGLE 17
equilateral TRIANGLE, area 17, side: ...
{{ site.hwprompt }} ./shapes.py SQUARE 8
SQUARE, area 8, side: ...
{{ site.hwprompt }} ./shapes.py CIRCLE 6
CIRCLE, area 6, radius: ...
{% endhighlight %}

When you have completed this, add it to your repository.

## Project Advice

The shape drawing project requires similar capabilities to the extended version of the homework.  Perhaps you want to reuse it?  If you wrote in it a way that is re-useable (which you should know how to do from the homework), then feel free to do so.
