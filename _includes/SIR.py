import scipy, scipy.integrate

# modified based on http://people.oregonstate.edu/~medlockj/other/python/SIR.py

# Parameters
from collections import namedtuple
Params = namedtuple('Params','beta gamma mu N0')
params = Params(beta=5, gamma=1, mu=1/50, N0=1)

S0, R0 = 0.99, 0.
I0 = params.N0 - S0 - R0
Y0 = [ S0, I0 ]

tMax = 100

T = scipy.linspace(0, tMax, 1001)

def dSIR(Y, t, beta, gamma, mu, N0):
    """
    SIR model, for const. pop.
    @param Y: [S, I]
    @param t: the time step
    @param beta, gamma, nu, N0: model parameters
    @return: [dS, dI]
    """
    S, I = Y

    dS = mu * N0 - beta * I * S - mu * S
    dI = beta * I * S - (gamma + mu) * I

    return [ dS, dI ]

# Integrate the ODE
# Warning!  The ODE solver over-writes the initial value.
solution = scipy.integrate.odeint(dSIR,
                                  Y0,
                                  T,
                                  args = params)
        
S = solution[:, 0]
I = solution[:, 1]
R = params.N0 - S - I

import pylab

pylab.figure()

pylab.plot(T, S,
           T, I,
           T, R)

pylab.xlabel('Time')
pylab.ylabel('Proportion')

pylab.legend([ 'Susceptible', 'Infective', 'Recovered' ])

pylab.show()
