Write a program `random_pi.py` that:

Receiving a seed and sample size, generates that many random numbers, uniformly sampled on 0 to 1.

Using those random numbers, estimate the value of `pi` by the circle-area method and then by the sphere-volume method.

You program should behave like:
{% highlight bash %}
{{ site.hwprompt }} ./random_pi.py 0 10000
circle-area pi: ...
sphere-volume pi: ...
{% endhighlight %}