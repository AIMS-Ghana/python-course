Implement the Mid-point approach to numerical integration in `midpoint.py`.

Consult `try_integrators.py` to understand the required method signatures.  Once your integrators are complete, the following
code should work:

~~~
{{ site.hwprompt }} ./try_integrators.py
...midpoint method, area under e^x on (0, 10), 100 points: ...
...scipy.integrate result: ...
~~~

Implement the bisection method for root finding with a stopping criteria on the value of the function (instead of the width of the interval) in `bisection.py`.  See `try_roots.py` for the appropriate method signature.  Once your code is complete, the following should work:

~~~
{{ site.hwprompt }} ./try_roots.py
...bisection method, root of y = (x-1)(x+10)^2 on (0, 10)
...scipy.optim result: ...
~~~