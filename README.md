# Simulation
Simulation workshop of course TIES481-20 / University of Jyväskylä. This is a 
hospital simulation, in which there are limited number of preparation rooms, 
operation rooms and recovery rooms. New patient arrives in every 10 minutes. 


## ASSIGNMENT 4

We ran 8 different sets of simulations with different configurations. 
Exact details of the configurations are found in the comments of main.py
What was varied was mainly the distributions of the structural variants.
Results were somewhat confusing as many sample sets taken from the simulations
showed no queue at all, and thus gave correlations of pure 0. And
if there was a queue, it gave somewhat increasing correlations as simulation
time went forward. 
That would mean that initial transient didn't go away. 
We tried increasing simulation time and changing sample sizes and intervals but
the increasing correlations remained, so somewhere something is bugging out but 
we couldn't find it. The other option is that we have some critical misunderstanding
regarding this assignment, which is certainly not ruled out.
Parts of the assignment were left undone due to time constraints.


## main.py
This is the thing you want to run. If you want to change simulation parameters,
change main.py

## simulation.py
Contains the code for the hospital simulation. Returns different information 
regarding the simulation.

If you need to change the preparation, surgery or recovery times, simulation.py 
has those parameters.

## stats.py
Contains the code for some statistics related functions


