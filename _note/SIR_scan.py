import scipy, scipy.integrate
import numpy as np

# modified based on http://people.oregonstate.edu/~medlockj/other/python/SIR.py

# Parameters
from collections import namedtuple
Params = namedtuple('Params','beta gamma mu N0')
params = Params(beta=5, gamma=2, mu=1/50, N0=1)

S0, R0 = 0.9, 0.05
I0 = params.N0 - S0 - R0
Y0 = [ S0, I0, R0 ]

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
    S, I, R = Y

    dS = mu * N0 - beta * I * S - mu * S
    dI = beta * I * S - (gamma + mu) * I
    dR = gamma*I - mu*R

    return [ dS, dI, dR ]


nsteps = 100
ulim = 3
muscan = np.linspace(0,ulim,nsteps)

# recovery_peaks = np.zeros(nsteps)

# Params(beta=5, gamma=2, mu=1/50, N0=1)

# for i in range(0, nsteps):
#     solution = scipy.integrate.odeint(dSIR,
#         Y0, T,
#         args = (params.beta, params.gamma, muscan[i], params.N0))
#     R = solution[:, 2]
#     recovery_peaks[i] = np.max(R)

result = [np.max(scipy.integrate.odeint(dSIR,
        Y0, T,
        args = (params.beta, params.gamma, mu, params.N0))[:,2]) for mu in muscan]
# Integrate the ODE
# Warning!  The ODE solver over-writes the initial value.

#print({'Smin':Smin, "Imax":Imax, 'Rmax':Rmax })

import pylab

pylab.figure()

pylab.plot(muscan, result)

pylab.xlabel('mu')
pylab.ylabel('Rpeak')

#pylab.legend([ 'Susceptible', 'Infective', 'Recovered' ])

pylab.show()
