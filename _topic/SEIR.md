---
title: SEIR Model Project
---

## Project Overview

You will write a program that will calculate the dynamics for an SEIR
system of differential equations.  That program should accept input in the form
of a `json` file and optional output targets for numerical and plotted results.

## File Format

### JSON Input

The format of the optional json file is (`+f` means non-negative floating point number, `++f` means strictly positive):

{% highlight json %}
{
  "beta": +f,
  "sigma": +f,
  "rho": +f,
  "mu": +f,
  "Y0": [+f, +f, +f, +f],
  "tmax": ++f
}
{% endhighlight %}

where *Y0 = (S0,E0,I0,R0)*.

If there is some input error, your program should provide a helpful error message.

### Numerical Output

The numerical output, whether to screen or csv, should begin with a header line,
then follow with the numerical values.  The first line should always be 0 followed
by the values for S0, E0, etc.  The last line should always be tmax, followed by the final
values for S, E, etc.

So results might look like:

{% highlight text %}
t, S, E, I, R
0, .99, 0, 0.01, 0
... etc ...
{% endhighlight %}

If no file for numerical output is provided, it should be output to the screen.

Your numerical results should be accurate to 1e-6 absolute tolerance or better.

### Plotting Output

The plot output should be a png, with one trajectory line for each S, E, I, R,
clearly labeled axes / legend, and useful scales.

If no file for plotting is provided, the code should save a "plot.png" file.

## Example Usage

In summary, you program should run as:

{% highlight bash %}
python-course-homework username$ ./SEIR.py
Error: no json file provided
python-course-homework username$ ./SEIR.py withnegativevalues.json
Error: the parameter input had negative values for whichever inputs
python-course-homework username$ ./SEIR.py -h
... useful info about usage ...
python-course-homework username$ ./SEIR.py config.json
... rows of numerical output, including header line ...
python-course-homework username$ ls plot.png
... finds plot you just made ...
python-course-homework username$ ./SEIR.py config2.json target.csv target.png
python-course-homework username$ ls target.*
... finds the csv and png you just created ...
{% endhighlight %}

## Process

As you make progress on this assignment, you should be committing updates to your
branch in the repository.

When you think you are ready, you should have committed all of your revisions and pushed
them to the repository.  Then email your TA indicating this project is ready for evaluation.

If you finish early, we can talk about extensions to the project.

On the last day of class, you should be prepared to demonstrate your project from the commandline.  You will probably want to create some json files to show different results.