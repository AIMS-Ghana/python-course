---
title: Project
---

## What

For the project, as previously mentioned, you will be working with the SIR model.

Recall:

{% include sir.liquid %}

What are the tools we have picked up from `numpy` and `scipy`?

 - random number generation (`np.random` functions)
 - ODE integration (`scipy.integrate` options)
 - roots, fitting (`scipy.optimize` options)

We can use these tools to a few ends:

 - stochastic simulation of this system
 - numerical integration to determine time series
 - parameter fitting from data

So, what are some examples of good project work?

 - how the trajectories change based on some parameter change
 - how the trajectories respond to different initial conditions
 - how stochastic results compare to the empirical ones
 - determining the model parameters from a data time series
 - comparing small modifications to the SIR model to the base model,
 *e.g.*, adding an **E**xposed compartment.

For an overview of solving dynamical systems using `scipy` and `numpy`, you should
refer to [this website](http://www.gribblelab.org/compneuro2012/2_Modelling_Dynamical_Systems.html).
I recommend that you actually follow through that example.

If you would like to try stochastic simulation, you should use the Gillespie
algorithm.
