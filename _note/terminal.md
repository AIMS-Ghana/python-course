---
title: Notes on Terminal Use
---
### Terminal Command Line Interface (CLI)

This class is not about mastery of the terminal, but you will need to use it, and
unless you use it all the time, you will need a refresher on what commands do what.

First, how do you get to the terminal?  On most linux machines `Ctrl-Shft-T` will open a terminal.
You can also right-click on a folder in the GUI, and you should see an option for "Open in Terminal".  Finally, on the icon bar, you probably can find an icon that looks like a black box with a `>_` in it.

When you open a terminal, the last line will be something like:

~~~
username@computername:current_directory$
~~~

Where `username` will be your username, `computername` is the computer you are at (something like `aimsgh123`), and `current_directory` will be the current directory you are in.  If you opened the terminal with a key combo, your directory is probably `~` which is shorthand for your home directory.

The most important command for figuring things out in the terminal is `man`, short for *manual*.  For example:

~~~
username@computername:current_directory$ man ls
~~~

will tell you how the `ls` command works in gory detail.  Investigate the following
commands about basic directory manipulation:

 - `ls`
 - `cd`
 - `mkdir`
 - `rm`
 - `rmdir`
 - `pwd`

There are a few important other filesystem symbols: `.`, `..`, and `~`.  I mentioned `~`
earlier; use `cd` and `ls` to figure out what `.` and `..` mean.

One other note about `.` - often, files or directories will start with `.`, like
`.ssh` from when we set up keys for Github.  These files and directories tend to correspond
to configuration info and application info (*e.g.*, cache or preferences), rather
than user content.

There are a few other basic commands that are important for working with files.  Again,
check these out with `man`:

 - `touch`
 - `cat`
 - `more`
 - `less`
 - `grep`
 - `chmod`
 - `mv`
 - `cp`

There are numerous other command line utilities, but these will probably be your
most-heavily used basic commands.

Two critical command line utilities for this course: `python3` and `pydoc3`.
