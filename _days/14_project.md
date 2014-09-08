---
title: Project
---

## What

For the project, as previously mentioned, you will be working with the SIR model.

Recall:

{% include sir.liquid %}

What are the tools we have picked up from `numpy` and `scipy`:

 - random number generation (`np.random` functions)

We will be implementing two approaches to thinking about a dynamical system:

 - using numerical solvers to approximate the system
 - using a stochastic approach, the Gillespie algorithm, to simulate the system

For an overview of solving dynamical systems using `scipy` and `numpy`, you should
refer to [this website](http://www.gribblelab.org/compneuro2012/2_Modelling_Dynamical_Systems.html).
I recommend that you actually follow through that example.

The Gillespie algorithm is basically:

 - sum the rates of all possible events in the system (*i.e.* state transitions
   and system in-out flows)
 - using that rate, draw an exponentially distributed time; this corresponds to
 how long it took for an event to occur
 - determine which event occurred by drawing between the different rates weighted
 by their ratios to the total rate
 - advance the system by time and event, and repeat (until particular time or state is reached)

## How

Represent the **SIR** model equations in a format suitable for solving with `scipy`.

Represent the **SIR** model transitions and rates
