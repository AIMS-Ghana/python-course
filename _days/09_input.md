---
title: "Input: Interactive and Files"
prep: lists
---

## Command Line Input

Recall how we use python scripts from the console:

~~~
$ python3 somescript.py [...optional arguments]
~~~

Inside the script, we can access these optional arguments in a special way:

{% include pyblock.md target="input_cl.py" %}

(note: when running with PyCharm, I had to edit the run configuration to pass
arguments.  This is the input field below the script name)

Note a few points:

 - the script call itself is the first argument
 - the rest of the arguments are string values, even though we provided some numbers

When we just need to provide a series of arguments in a fixed format, this approach
will do nicely.  However, if we want to use our Python script more like a command line
utility like `ls`, we should be able to support a more complicated syntax:

~~~
$ somecommand -xvf --target="thing" 1 2 3
~~~

Writing a parser for this is *quite* fiddly.  Fortunately, there is a built in
module for addressing this problem, `argparse`:

{% include pyblock.md target="input_cl2.py" %}

Still complex, but not nearly as complex as writing it yourself.  And `argparse`
automatically handles providing a useful help option and will complain sensibly when offered
incorrect arguments.

## User Input

Often, we want to interact with a program, like for example the Python REPL.  Here
is a simple input-output loop:

{% include pyblock.md target="input_user.py" %}

We use the `input(\...)` command to prompt the user for input, but must be careful
as what is submitted is always a string in this version.

## File Input

The other typical input case is that we have a file of data which we want to use
rather than directly coding which particular values we want to evaluate with
our programs.

{% include pyblock.md target="input_file.py" %}

## Task: Input!

We are going to combine all three of these methods into a single program. You
will write a Python script that is intended to run from the command line:

~~~
$ python3 shaper.py [-(h|f|i)]
~~~

This script will provide a user geometric properties in response to their input
about what shapes they want the properties for, and the dimensions of those
shapes.  That input can either be interactive or from a file.

* * *

This is a fairly complex program, so you should proceed with small steps
verifying the pieces as you go along.  You should also implement the program from easiest
part to hardest, which in this case is probably a bit *backwards* relative to what will
actually happen in the program.

 - first, finish your classes for the shapes.
 - then, for a particular shape, figure out how to turn an array of string inputs
 (*e.g.*, `['3.7', '1.5', '6', ...]`) into one of those objects.
 - then, figure out to use a similar array (*e.g.*, `['circle', '1.5']`), to pick
 the correct shape **and** create it.
 - make sure that your program can handle junk inputs via `try-except`, since you
 will need to notify users of errors *without* crashing out of the program
 - next, re-arrange the user input and file input examples to get those input
 arrays via the interfaces described below; you will probably want to make a test csv,
 which can be done with any text editor
 - almost finally, write the connections between these parts
 - and finally, write the code that handles launching the script

Both parts of this whole task are asking for the same kind of thing, just with a
different input mode.  Try to separate the input and evaluation parts of the
program (as described above), so that you can re-use the evaluation part.

### Command Line Mode:

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
If the input line is invalid, instead of a line about a shape, the script should
print a line explaining the error with that line of input.

### Twist: Output!

Add an `-o` option to be used with `-f` that specifies the output file.  Instead
of printing the output results, write them as lines in the output file.
