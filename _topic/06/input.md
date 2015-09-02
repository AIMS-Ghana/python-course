---
title: Input and Output
hw: true
warmup: true
---
{% include startup.md %}

## Command Line Input

Recall how we use python scripts from the console:

~~~
$ ./somescript.py [...optional arguments]
~~~

Inside the script, we can access these optional arguments in a special way:

{% include relblock.md target="input_cl.py" %}

(note: when running with PyCharm, I had to edit the run configuration to pass
arguments.  This is the input field below the script name)

Recall:

 - the script name itself is the first argument
 - the rest of the arguments are string values, even though we provided some numbers

When we just need to provide a series of arguments in a fixed format, this approach
will do nicely.  However, if we want to use our Python script more like a command line
utility like `ls`, we should be able to support a more complicated syntax:

~~~
$ somecommand -xvf --target="thing" 1 2 3
~~~

Writing a parser for this is *quite* fiddly.  Fortunately, there is a built in
module for addressing this problem, `argparse`:

{% include relblock.md target="input_cl2.py" %}

Still complex, but not nearly as complex as writing it yourself.  And `argparse`
automatically handles providing a useful help option and will complain sensibly when offered
incorrect arguments.

## User Input

Often, we want to interact with a program, like for example the Python REPL.  Here
is a simple input-output loop:

{% include relblock.md target="input_user.py" %}

We use the `input(\...)` command to prompt the user for input, but must be careful
as what is submitted is always a string in this version.

## File Input

The other typical input case is that we have a file of data which we want to use
rather than directly coding which particular values we want to evaluate with
our programs.

{% include relblock.md target="input_file.py" %}