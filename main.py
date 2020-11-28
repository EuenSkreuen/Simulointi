# -*- coding: utf-8 -*-
"""
TIES481: Simulation

Created on Sat Nov 21 17:34:23 2020

@author: Janne Heikkinen, Aapo Peiponen ja Liisa Petäinen

"""

import simulation
import stats
import randomize

#TODO: random seeds actually random (currently they are 1,2,3,4,...)
#TODO: probability of all recovery rooms being blocked?
#TODO: pairwise comparisons with same random seeds

#PART 1
#Runs 20 independent samples for given 3 different configurations

#3 preparation rooms with 4 recovery rooms
print("\r\n\r\n")
for i in range(1,20):
    simulation_length = 1000
    results = simulation.run_simulation(3,4,10,40,40,simulation_length, i, False)
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
    

#3 preparation rooms with 5 recovery rooms
print("\r\n\r\n")
for j in range(21,40):
    simulation_length = 1000
    results = simulation.run_simulation(3,5,10,40,40,simulation_length, j, False)
    avg = stats.mean(results[0]) 
    conf = stats.confidence95(results[0])
    lower_bound = conf[0]
    upper_bound = conf[1]
    print("The average preparation queue length is %.2f with a 95%% confidence interval of [%.2f , %.2f]." % (avg, lower_bound, upper_bound))
    operation_idle_time = results[1]
    operation_idle_percentage = operation_idle_time / simulation_length * 100
    print("Operation room was idle for %.0f time units, meaning the total probability of it being blocked at random time unit is %.2f %%" % (operation_idle_time, operation_idle_percentage))
    
    recovery_blocked = results[2] / results[3] * 100
    print("The probability of recovery being full and operation being blocked is: ", recovery_blocked)

#4 preparation rooms with 5 recovery rooms
print("\r\n\r\n")
for k in range(41,60):
    simulation_length = 1000
    results = simulation.run_simulation(4,5,10,40,40,simulation_length, k, False)
    avg = stats.mean(results[0])
    conf = stats.confidence95(results[0])
    lower_bound = conf[0]
    upper_bound = conf[1]
    print("The average preparation queue length is %.2f with a 95%% confidence interval of [%.2f , %.2f]." % (avg, lower_bound, upper_bound))
    operation_idle_time = results[1]
    operation_idle_percentage = operation_idle_time / simulation_length * 100
    print("Operation room was idle for %.0f time units, meaning the total probability of it being blocked at random time unit is %.2f %%" % (operation_idle_time, operation_idle_percentage))
    
    recovery_blocked = results[2] / results[3] * 100
    print("The probability of recovery being full and operation being blocked is: ", recovery_blocked)


"""

Assignment 4

- Interarrival times can be either exponentially or uniformly distributed with 
  two different possible average arrival rates (exp(25) or exp (22.5),  Unif(20,30) or Unif(20,25))

- Preparation time can be either exp(40) or Unif(30,50)

- Recovery time can be either exp(40) or Unif(30,50)

- There can be either 4 or 5 preparation units

- There can be either 4 or 5 recovery units

"""



"""

interarrival_time is either exp(25) or exp(22.5)

prep_time is either exp(40) or unif(30,50)
rec_time is either exp(40) or unif(30,50)
number of preparation rooms is either 4 or 5
number of recovery rooms is either 4 or 5

"""

print("\r\n\r\n")
for k in range(61,80):
    
    simulation_length = 1000
    
    interarrival_time = random.choice([randomize.exponential(25), randomize.exponential(22.5)])
    prep_time = random.choice([randomize.exponential(40), randomize.unif(30,50)])
    rec_time = random.choice([randomize.exponential(40), randomize.unif(30,50)])
    results = simulation.run_simulation(random.choice([4,5]), random.choice([4,5])
                    , interarrival_time, prep_time, rec_time, simulation_length, k, False)
    
    avg = stats.mean(results[0])
    conf = stats.confidence95(results[0])
    lower_bound = conf[0]
    upper_bound = conf[1]
    print("The average preparation queue length is %.2f with a 95%% confidence interval of [%.2f , %.2f]." % (avg, lower_bound, upper_bound))
    operation_idle_time = results[1]
    operation_idle_percentage = operation_idle_time / simulation_length * 100
    print("Operation room was idle for %.0f time units, meaning the total probability of it being blocked at random time unit is %.2f %%" % (operation_idle_time, operation_idle_percentage))
    
    recovery_blocked = results[2] / results[3] * 100
    print("The probability of recovery being full and operation being blocked is: ", recovery_blocked)
    

"""

interarrival_time is either unif(25) or unif(22.5)

prep_time is either exp(40) or unif(30,50)
rec_time is either exp(40) or unif(30,50)
number of preparation rooms is either 4 or 5
number of recovery rooms is either 4 or 5

"""

print("\r\n\r\n")
for k in range(61,80):
    
    simulation_length = 1000
    
    interarrival_time = random.choice([randomize.unif(20,30), randomize.unif(20,25)])
    prep_time = random.choice([randomize.exponential(40), randomize.unif(30,50)])
    rec_time = random.choice([randomize.exponential(40), randomize.unif(30,50)])
    results = simulation.run_simulation(random.choice([4,5]), random.choice([4,5])
                    , interarrival_time, prep_time, rec_time, simulation_length, k, False)
    
    avg = stats.mean(results[0])
    conf = stats.confidence95(results[0])
    lower_bound = conf[0]
    upper_bound = conf[1]
    print("The average preparation queue length is %.2f with a 95%% confidence interval of [%.2f , %.2f]." % (avg, lower_bound, upper_bound))
    operation_idle_time = results[1]
    operation_idle_percentage = operation_idle_time / simulation_length * 100
    print("Operation room was idle for %.0f time units, meaning the total probability of it being blocked at random time unit is %.2f %%" % (operation_idle_time, operation_idle_percentage))
    
    recovery_blocked = results[2] / results[3] * 100
    print("The probability of recovery being full and operation being blocked is: ", recovery_blocked)



