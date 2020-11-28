# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 12:44:00 2020

@author: Aapo Peiponen ja Liisa Petäinen


"""

import random

# returns the exponentially distributed random number of desired mean
def exponential(mean):
    lambd = 1.0 / mean
    return random.expovariate(lambd)

# returns the uniformly distributed random number of desired range
def unif(a, b):
    return random.uniform(a,b)



