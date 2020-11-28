# Simulation
Simulation workshop of course TIES481-20 / University of Jyväskylä. This is a 
hospital simulation, in which there are limited number of preparation rooms, 
operation rooms and recovery rooms. New patient arrives in every 10 minutes. 

####ASSIGNMENT 3######

- No major differences detected with different configurations. Changed interarrival time to 10 because results didnt make sense with 25 for some reason.

- Pairwise comparisons didn't show major differences. 3p4r and 3p5r had similar queue length, while 4p5r had slightly shorter queue.

- Recovery blocking operation remains unsure

######################



## ASSIGNMENT 4

- Aapo: lisätty randomize-luokka
- simulation.py:lle viedään muuttujina myös ne interarrival-, preparation- ja recovery-ajat

- kaksi simulaatiota lisätty, erot interrival_time:n arvontatyylissä
- ensimmäinen simu: 
    - interarrival_time is **either exp(25) or exp(22.5)**
    - prep_time is either exp(40) or unif(30,50)
    - rec_time is either exp(40) or unif(30,50)
    - number of preparation rooms is either 4 or 5
    - number of recovery rooms is either 4 or 5
 
 - ja toinen:
    - interarrival_time is **either unif(25) or unif(22.5)**
    - prep_time is either exp(40) or unif(30,50)
    - rec_time is either exp(40) or unif(30,50)
    - number of preparation rooms is either 4 or 5
    - number of recovery rooms is either 4 or 5

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

## TODO

- priorities
- monitoring - does SimPy have it's own monitoring-unit we could use?
- maybe write more comments inside the code
