# -*- coding: utf-8 -*-
"""
TIES481: Simulation

Created on Sat Nov 21 17:34:23 2020

@author: Janne Heikkinen, Aapo Peiponen ja Liisa Petäinen

"""

import simulation
import stats
#TODO: random seeds actually random (currently they are 1,2,3,4,...)

def simulate(p, r, seed):
    """
    This is here just to save some space
    """
    simulation_length = 1000
    results = simulation.run_simulation(p,r,simulation_length, seed, False)
    avg = stats.mean(results[0]) #average of preparation queue
    conf = stats.confidence95(results[0]) #confidence interval of preparation queue
    lower_bound = conf[0]
    upper_bound = conf[1]
    print("The average preparation queue length is %.2f with a 95%% confidence interval of [%.2f , %.2f]." % (avg, lower_bound, upper_bound))
    operation_idle_time = results[1] #total operation room idle time
    operation_idle_percentage = operation_idle_time / simulation_length * 100 #percentage of operation idle time to total simulation time  
    print("Operation room was idle for %.0f time units, meaning the total probability of it being blocked at random time unit is %.2f %%" % (operation_idle_time, operation_idle_percentage))
    
    recovery_blocked = results[2] / results[3] * 100
    print("The probability of recovery being full and operation being blocked is: ", recovery_blocked)

#3 preparation rooms with 4 recovery rooms
print("\r\n\r\n")
for i in range(1,20):
    simulate(3, 4, i)

#3 preparation rooms with 5 recovery rooms
print("\r\n\r\n")
for j in range(21,40):
    simulate(3, 5, j)

#4 preparation rooms with 5 recovery rooms
print("\r\n\r\n")
for k in range(41,60):
    simulate(4, 5, k)

#Pairwise comparisons
print("\r\n\r\n")
print("\r\n\r\n")

s = 100
print("\r\nResults for 3p4r and 3p5r:")
simulate(3,4,s)
simulate(3,5,s)
print("\r\nResults for 3p4r and 4p5r:")
simulate(3,4,s)
simulate(4,5,s)
print("\r\nResults for 3p5r and 4p5r:")
simulate(3,5,s)
simulate(4,5,s)





