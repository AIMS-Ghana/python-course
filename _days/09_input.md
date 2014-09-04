---
title: "Input: Interactive and Files"
prep: lists
---

## User Input

Often, we want to interact with a program, like for example the Python REPL.  Here
is a simple input-output loop:

{% include pyblock.md target="input_user.py" %}

We use the `input(\...)` command to prompt the user for input, but must be careful
as what is submitted is always a string in this version.

## File Input

## Task: Input!

Write a Python script that is intended to run from the command line, ala:

~~~
$ python3 yourscript.py [...optional arguments]
~~~

This script will provide a user geometric properties in response to their input
about what shapes they want the properties for, and the dimensions of those
shapes.

Your script should receive three arguments:

 - `-h` for \"help\", which will print information about the script and script
 options
 - `-i` for \"interactive\" mode, which will respond directly to user requests
 - `-f` for \"file\" input, which should be followed by a filename

If the script receives erroneous arguments, it should respond with the results
of `-h`.

I recommend you review this [built in module](https://docs.python.org/3/library/argparse.html#module-argparse) for
that part of the task.

### Interactive Mode:

In interactive mode, the script should indicate which shapes can be calculated,
and prompt the user to select one by entering its name, as well as offering an
option to quit.

If the user enters something other than one of the available shapes or quit, the
script should remind the user what shapes are available and about the quit option,
then prompt the user to select one.

If the user selects an available shape, they should be prompted with the dimension
options for that shape and an option to return to the shapes prompt or quit.
If they enter appropriate dimensions, the resulting geometric properties should be
displayed, then the user should be returned to the shapes prompt.  In they enter
bad input, they should be reminded what the dimension options are, and
returned to that prompt.

### File Mode:

In file mode, the script should scan through a file containing lines like:

~~~
square 5.7
triangle 4 10.0
right-cylinder 5 10
...
~~~

and for each line, read in the requested shape and dimensions, and respond with
the shape, its dimensions, and its geometric properties (this should be exactly
the `__str__` method results for the corresponding `Shape` class you wrote).
If the input line is invalid, instead of line about a shape, the script should
print a line explaining the error with that line of input.

### Advice:

Both parts of this task are asking for the same kind of thing, just with a
different input mode.  Try to separate the input and evaluation parts of the
program, so that you can re-use the evaluation part.
