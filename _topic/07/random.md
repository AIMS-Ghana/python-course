---
title: Pseudo-Random Numbers
hw: true
warmup: true
math: true
---
{% include startup.md %}

## Key Research Idea

"Real" random numbers *vs*. pseudo-random numbers: in scientific research, we
will often treat some phenomena as having a random component.  Sometimes that means
truly random (we're pretty sure this is what is going on with quantum effects),
some times it means random as far as we can tell (maybe we just haven't measured all the right pieces), sometimes it means random for modeling purposes (chaos can be treated this way).

And that last point brings us round to pseudo-random numbers - they are meant to
be "random as far as we can tell", but also deterministically generable - that's
basically chaos, but with extreme attractor cycle lengths and paths.

## Advanced Work

You may or may not have recognized, but you just performed your first Monte Carlo
simulation.  Now we will do Markov Chain Monte Carlo using Gillespie's Method
on the Lotke-Volterra Equations (*a/k/a*, the predator-prey model).

$$
\dot{x} = \alpha x - \beta xy\\
\dot{y} = \delta xy - \gamma y
$$

Gillespie's method is about:

1. Using *rate of any event* = *sum of rate of all possible events* to determine
time-between-events, and
2. determining *which event*, with probability proportional to their rates.

So:

$$
\lambda = \sum_i \lambda_i \\
t \sim e^{-\lambda} \\
p_i \sim {\lambda_i \over \lambda}
$$

The rates are:

| event |    rate     |
|:-----:|:-----------:|
|  +x   | $\alpha x$  |
|  -x   | $\beta xy$  |
|  +y   | $\delta xy$ |
|  -y   | $\gamma y$  |

so the waiting time for any state is

$$
\lambda = \alpha x + \gamma y + xy(\beta + \delta) \\
t \sim Exp(\lambda)
$$

and the probabilities of which event occurred at that time are

| event |            rate             |
|:-----:|:---------------------------:|
|  +x   | ${\alpha x \over \lambda}$  |
|  -x   | ${\beta xy \over \lambda}$  |
|  +y   | ${\delta xy \over \lambda}$ |
|  -y   | ${\gamma y \over \lambda}$  |
