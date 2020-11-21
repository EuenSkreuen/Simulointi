# -*- coding: utf-8 -*-
"""
TIES481: Simulation

Created on Sat Nov 21 17:34:23 2020

@author: Janne Heikkinen, Aapo Peiponen ja Liisa Petäinen

"""

import simulation
import stats
#TODO: random seeds actually random (currently they are 1,2,3,4,...)
#TODO: probability of all recovery rooms being blocked?
#TODO: pairwise comparisons with same random seeds

#PART 1
#Runs 20 independent samples for given 3 different configurations

#3 preparation rooms with 4 recovery rooms
print("\r\n\r\n")
for i in range(1,20):
    simulation_length = 1000
    results = simulation.run_simulation(3,4,simulation_length, i, False)
    avg = stats.mean(results[0]) #average of preparation queue
    conf = stats.confidence95(results[0]) #confidence interval of preparation queue
    lower_bound = conf[0]
    upper_bound = conf[1]
    print("The average preparation queue length is %.2f with a 95%% confidence interval of [%.2f , %.2f]." % (avg, lower_bound, upper_bound))
    operation_idle_time = results[1] #total operation room idle time
    operation_idle_percentage = operation_idle_time / simulation_length * 100 #percentage of operation idle time to total simulation time
    print("Operation room was idle for %.0f time units, meaning the total probability of it being blocked is %.2f %%" % (operation_idle_time, operation_idle_percentage))

#3 preparation rooms with 5 recovery rooms
print("\r\n\r\n")
for j in range(21,40):
    simulation_length = 1000
    simulation.run_simulation(3,5,simulation_length, j, False)
    avg = stats.mean(results[0]) 
    conf = stats.confidence95(results[0])
    lower_bound = conf[0]
    upper_bound = conf[1]
    print("The average preparation queue length is %.2f with a 95%% confidence interval of [%.2f , %.2f]." % (avg, lower_bound, upper_bound))
    operation_idle_time = results[1]
    operation_idle_percentage = operation_idle_time / simulation_length * 100
    print("Operation room was idle for %.0f time units, meaning the total probability of it being blocked is %.2f %%" % (operation_idle_time, operation_idle_percentage))

#4 preparation rooms with 5 recovery rooms
print("\r\n\r\n")
for k in range(41,60):
    simulation_length = 1000
    simulation.run_simulation(4,5,simulation_length, k, False)
    avg = stats.mean(results[0])
    conf = stats.confidence95(results[0])
    lower_bound = conf[0]
    upper_bound = conf[1]
    print("The average preparation queue length is %.2f with a 95%% confidence interval of [%.2f , %.2f]." % (avg, lower_bound, upper_bound))
    operation_idle_time = results[1]
    operation_idle_percentage = operation_idle_time / simulation_length * 100
    print("Operation room was idle for %.0f time units, meaning the total probability of it being blocked is %.2f %%" % (operation_idle_time, operation_idle_percentage))



