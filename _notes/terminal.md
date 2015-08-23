---
title: Notes on Terminal Use
---
### Terminal Command Line Interface (CLI)

Last session, we used the terminal to enable more convenient access to GitHub.

This class is not about mastery of the terminal, but you will need to use it, and
unless you use it all the time, you will need a refresher on what commands do what.

The most important command for that purpose is `man`, short for *manual*.  For example:

~~~
computername:~ username$ man ls
~~~

will tell you how the `ls` command works in gory detail.  Investigate the following
commands about basic directory manipulation, and then there will be a quiz:

 - `ls`
 - `cd`
 - `mkdir`
 - `rm`
 - `rmdir`
 - `pwd`

There are a few important other filesystem symbols: `.`, `..`, and `~`.  I mentioned `~`
in the previous session; use `cd` and `ls` to figure out what `.` and `..` mean.

One other note about `.` - often, files or directories will start with `.`, like
`.ssh` in the previous session.  These files and directories tend to correspond
to configuration info and application info (*e.g.*, cache or preferences), rather
than user content.

There are a few other basic commands that are important for working with files.  Again,
check these out with `man`, and then there will be a quiz:

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

Two critical command line utilities for this course: `python3` and `pydoc3`.  We
will learn more about those in a bit.
