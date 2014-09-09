__author__ = 'cap10'

import numpy as np

def dSIR(Y, beta, gamma, mu, N0):
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


from collections import namedtuple
Params = namedtuple('Params','beta gamma mu N0')
params = Params(beta=5, gamma=1, mu=1/50, N0=1)

from scipy.optimize import root

print(root(dSIR,x0=[0.5, 0.5],args=params))