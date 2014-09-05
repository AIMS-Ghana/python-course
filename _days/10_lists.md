---
title: "Collections"
prep: review
math: yes
---

## What is the form of data from experiments?

For many equations, we have a few parameters that determine system state.  The
dynamics of a simple spring-mass system, *e.g.*, are determined by ultimately
a single parameter:

\begin{align}
\ddot{x} = -{k \over m}x \rightarrow {k \over m} = \omega^2
\end{align}

But the physical world is quite messier than that single parameter.  If want to
determine \{\omega\} for some actual spring mass (ignoring that the actual
physics are more complicated than this idealization), we need to gather many
data points both to actually solve the equation, but also to account for
measurement error.

Which is to say, real data are quite a bit more complex than the mostly single
variables we have been working with so far.  They tend to have many samples, and
samples tend to be a mixture of types of things.  Often times there are samples
of different kinds of things.

So in general, we need to be able to work with \"collections\" of things.

## Python Built-in Collections

Python has several built-in collections, serving different purposes.  They are
either sequential (`tuple`, `list`, `range`) or not (`dict`, `set`).

### `tuple`

A `tuple` is

{% include pyblock.md target="colls_tuples.py" %}

\... a sequence of things, not necessarily the same type.  You use a tuple when
you need a sequence, but do *not* need to change what is in the sequence.

### `list`

A `list` is a

{% include pyblock.md target="colls_list.py" %}

\... *also* a sequence of things, not necessarily the same type.  *However*, you
can change the contents of a `list`, either adding, deleting or replacing elements.

### `range`

You have already worked with `range(...)` a few times.  How do `ranges` compare
to `tuple`s and `list`s?

### `set`

A `set` is

{% include pyblock.md target="colls_set.py" %}

\... *not* a sequence of things, but like `tuple`s and `list`s, the things can
be different types.  *However*, only unique things appear in the set.  We can
still loop over the contents of a `set` but there are no guarantees about the order.

### `dict`

A `dict` is

{% include pyblock.md target="colls_dict.py" %}

\... also *not* a sequence of things, but as always, the things can
be different types.  Most notably, a `dict` is a collection where you can look
things up by name:

{% highlight python %}
adict = { 'students':[], 'instructors':['Carl', 'Des'] }
print(adict['instructors'])
{% endhighlight %}

## Comprehensions

Comprehensions are a way to take these basic collections and filter or transfrom
them in a very compact syntax:

{% include pyblock.md target="colls_comps.py" %}
