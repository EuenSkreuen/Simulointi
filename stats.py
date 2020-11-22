# -*- coding: utf-8 -*-
"""
TIES481: Simulation

Created on Sat Nov 21 16:16:31 2020

@author: Janne Heikkinen, Aapo Peiponen ja Liisa Petäinen

"""

import math

def mean(values):
    """
    Calculates the mean of the given values with given weigths. 
    """
    sum = 0
    for value in values:
        sum += value
    return sum/len(values)

def standard_deviation(values):
    """
    Calculates the standard deviation of the given values.
    """
    average = mean(values)
    sum = 0
    for value in values:
        difference = value - average
        sum += pow(difference, 2)
    #Should this be considered variance or sample variance?
    variance = sum/len(values)
    return math.sqrt(variance)

def confidence95(values):
    """
    Calculates confidence interval for 95% confidence level given the values
    """
    n = len(values)
    x = mean(values)
    s = standard_deviation(values)
    z = 1.96
    return (x-z*(s/math.sqrt(n)), x+z*(s/math.sqrt(n)))