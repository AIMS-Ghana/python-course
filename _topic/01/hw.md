Write programs, `triangle.py`, `rectangle.py`, `circle.py` that work as follows:

{% highlight bash %}
{{ site.hwprompt }} ./triangle.py 1 1 1
area 0.433
perimeter 3
{{ site.hwprompt }} ./rectangle.py 5 3
area 15
perimeter 16
{{ site.hwprompt }} ./rectangle.py 5
area 25
perimeter 20
{{ site.hwprompt }} ./circle.py 2
area 12.56
perimeter 12.56
{% endhighlight %}

These programs should also provide a useful error if given nonsensical inputs (e.g., negative side lengths, impossible triangles) or no inputs.

Additionally, the file `basic_shapes.py` (already implemented, no need to fiddle with it) should now work as follows:

{% highlight bash %}
{{ site.hwprompt }} ./basic_shapes.py
Equilateral Triangle, side 4:
a: ..., p: ...
Square, side 4:
a: ..., p: ...
Rectange, sides 4, 5:
a: ..., p: ...
Circle, radius 3:
a: ..., p: ...
{% endhighlight %}

The `basic_shapes.py` file imports those other files, so you will need to examine it to know what function names to use.

As you work through this homework, you should consider committing your incremental progress.  For example,
when you get the input parsing working for triangles:

{% highlight bash %}
{{ site.hwprompt }} git add triangle.py
{{ site.hwprompt }} git commit -m "implement triangle input parsing"
{{ site.hwprompt }} git push
{% endhighlight %}