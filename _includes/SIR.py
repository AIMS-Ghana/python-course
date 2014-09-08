#!/usr/bin/env python
#
# The above allows this script to be run directly from the shell
#

# This loads some pacakges that have arrays etc and the ODE integrators
import scipy, scipy.integrate

# modified based on http://people.oregonstate.edu/~medlockj/other/python/SIR.py

# Parameters
beta = 5
gamma = 1
mu = 1 / 50

# Initial condition
S0 = 0.99
R0 = 0.
I0 = 1 - S0 - R0

N0 = S0 + I0 + R0

Y0 = [ S0, I0 ]

tMax = 100

# Time vector for solution
T = scipy.linspace(0, tMax, 1001)


# This defines a function that is the right-hand side of the ODEs
# Warning!  Whitespace at the begining of a line is significant!
def dSIR(Y, t, beta, gamma, mu, N0):
    '''
    SIR model.
    
    This function gives the right-hand sides of the ODEs.
    '''
    
    # Convert vector to meaningful component vectors
    # Note: Indices start with index 0, not 1!
    S, I = Y

    # The right-hand sides
    dS = mu * N0 - beta * I * S - mu * S
    dI = beta * I * S - (gamma + mu) * I
    
    # Convert meaningful component vectors into a single vector
    dY = [ dS, dI ]

    return dY

# Integrate the ODE
# Warning!  The ODE solver over-writes the initial value.
# This can be a pain in the ass if you run the ODE multiple times.
# Also, 'args' passes parameters to right-hand-side function.
solution = scipy.integrate.odeint(dSIR,
                                  Y0,
                                  T,
                                  args = (beta, gamma, mu, N0))
        
S = solution[:, 0]
I = solution[:, 1]
R = N0 - S - I

# Make plots

# Load a plotting package
# PyLab is motivated by Matlab...
import pylab

# I usually use PyLab for quick plots
# and the Python GnuPlot package for publication

pylab.figure()

pylab.plot(T, S,
           T, I,
           T, R)

pylab.xlabel('Time')
pylab.ylabel('Proportion')

pylab.legend([ 'Susceptible', 'Infective', 'Recovered' ])

# Actually display the plot
pylab.show()
