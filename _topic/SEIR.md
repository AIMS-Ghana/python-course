---
title: SEIR Model Project
math: true
---

## Project Overview

You will write a program that will calculate the dynamics for an SEIR
system of differential equations and stochastic simulations of that same system (the Gillespie model).  That program should accept input in the form
of a `json` file and optional output targets for numerical and plotted results.

### The Constant Population SEIR Model

$$
S + E + I + R = N, \dot{N} = 0 \\
\dot{S} = \mu N - {\beta S I \over N} - \mu S\\
\dot{E} = {\beta S I \over N} - \sigma E - \mu E\\
\dot{I} = \sigma E - \gamma I - \mu I\\
\dot{R} = \gamma I - \mu R
$$

Feel free to re-arrange these equations as you see fit when implementing the system, but the result must be the same model.

## References

For an overview of solving dynamical systems using `scipy` and `numpy`, you should
refer to [this website](http://www.gribblelab.org/compneuro2012/2_Modelling_Dynamical_Systems.html).
I recommend that you actually follow through that example.  There is also an [example on the course page]({% include url.lq %}/topic/numpy-scipy/).

For Gillespie's algorithm and it's relation to ODE model, [see this discussion](http://plaza.ufl.edu/pulliam/training/icddrb/Welcome_files/Pulliam_ICDDRB_Day2.pdf)

## File Format

### JSON Input

The format of the optional json file is (`+f` means non-negative floating point number, `++f` means strictly positive, `+i` means non-negative integer):

{% highlight json %}
{
  "beta": +f,
  "sigma": +f,
  "gamma": +f,
  "mu": +f,
  "Y0": [+i, +i, +i, +i],
  "tmax": ++f
}
{% endhighlight %}

where *Y0 = (S0,E0,I0,R0)*.

If there is some input error, your program should provide a helpful error message.  Here are two files,
one that should work and one that should return an error: [works]({% include linkmunge.lq %}/params.json) and [does not]({% include linkmunge.lq %}/params.json)

### Numerical Output

The numerical output, whether to screen or csv, should begin with a header line,
then follow with the numerical values.  The first line should always be 0 followed
by the values for S0, E0, etc.  The last line should always be tmax, followed by the final
values for S, E, etc.

So results might look like:

{% highlight text %}
t, S, E, I, R
0, 99, 0, 1, 0
... etc ...
{% endhighlight %}

If no file for numerical output is provided, it should be output to the screen.

The program should accept a `-g N` option, which means produce N Gillespie simulations.  The format for simulation output should be:

{% highlight text %}
n, t, S, E, I, R
0, 0, 99, 0, 1, 0
... etc ...
{% endhighlight %}

where *n* identifies the run number.

Your numerical results should be accurate to 1e-6 absolute tolerance or better.

### Plotting Output

The plot output should be a png, with one trajectory line for each S, E, I, R,
clearly labeled axes / legend, and useful scales.

If no file for plotting is provided, the code should save a "plot.png" file.

## Example Usage

In summary, you program should run as:

{% highlight bash %}
{{ site.hwprompt }} ./SEIR.py badparams.json
Error: ... e.g., the parameter input had negative values for whichever inputs ...
{{ site.hwprompt }} ./SEIR.py
... same as next line ...
{{ site.hwprompt }} ./SEIR.py -h
... useful info about usage ...
{{ site.hwprompt }} ./SEIR.py config.json
... rows of numerical output, including header line ...
{{ site.hwprompt }} ls plot.png
... finds plot you just made ...
{{ site.hwprompt }} ./SEIR.py config2.json target.csv target.png
{{ site.hwprompt }} ls target.*
... finds the csv and png you just created ...
{{ site.hwprompt }} ./SEIR.py config2.json -g 10 target.csv target.png
{{ site.hwprompt }} ls target.*
... finds the csv and png you just created, should be Gillespie runs ...
{% endhighlight %}

## Process

As you make progress on this assignment, you should be committing updates to your
branch in the repository.

When you think you are ready, you should have committed all of your revisions and pushed
them to the repository.  Then email your TA indicating this project is ready for evaluation.

If you finish early, we can talk about extensions to the project.

On the last day of class, you should be prepared to demonstrate your project from the commandline.  You will probably want to create some json files to show different results.