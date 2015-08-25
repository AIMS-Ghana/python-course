Implement the Mid-point, Trapezoid, and Simpson's Method approaches to numerical integration in `midpoint.py`.

Consult `try_integrators.py` to understand the required method signatures.  Once your integrators are complete, the following
code should work:

~~~
{{ site.hwprompt }} ./try_integrators.py
Mid-Point Method, area under e^x on (0, 10), 100 points: ...
scipy.integrate result: ...
~~~

Implement the bisection method for root finding with a stopping criteria on the value of the function (instead of the width of the interval) in `bisection.py`.  See `try_bisection` for the appropriate method signature.  Once your code is complete, the following should work:

~~~
{{ site.hwprompt }} ./try_bisection.py
Bisection Method, root of ..., tolerance ...; root at: ...
scipy.optim result:
~~~