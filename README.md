# Simulation
Simulation workshop of course TIES481-20 / University of Jyväskylä. This is a 
hospital simulation, in which there are limited number of preparation rooms, 
operation rooms and recovery rooms. New patient arrives in every 10 minutes. 


## ASSIGNMENT 4

- lisätty randomize-luokka
- simulation.py:lle viedään muuttujina myös ne interarrival-, preparation- ja recovery-ajat
- joka simulaatiossa näille muuttujille omat säädöt

- 8 erilaista konfiguraatiota simuloitu
    - näistä pitäisi ilmeisesti päätellä, mikä voisi olla lähemmän tarkastelun arvoinen
    - jos oikein käsitin, lyhyt jono siihen preparationiin olisi tavoitteltava piirre
    - en tehnyt mitään tarkempia analyysejä vielä, mutta silmämääräisesti näyttäisi, että 
    conffit 3,4,7 ja 8 näyttää parhaimmalta?
    
    - vois nuo conffit jotenkin lyhyemmästikin koodata, esim. jos laittais ne eri vaihtoehdot johki
    taulukkoon ja poimis sieltä, mutta menköön nyt noin
    - näissä kaikissa konfiguraatiossa on tällä hetkellä huoneiden määrä 4,5
    - vois tulla enemmän vertailtavaa esim. 4,4 -asetuksella
    
- To do:
    - run several (say 10) independent simulation runs taking several (say 10 again) samples 
    (keeping the order is important here)
        - jotta tän vois tehdä, pitää joku tehdä taulukkohärveli, mihin nämät järjestyksessä tallentuu?
    - compute the correlations between the elements of these series
    - Observe the average length of the queue on arrival (i.e before preparation) as this queue
    forms a memory between samples that are taken too close to each other

#
#
    

####ASSIGNMENT 3######

- No major differences detected with different configurations. Changed interarrival time to 10 because results didnt make sense with 25 for some reason.

- Pairwise comparisons didn't show major differences. 3p4r and 3p5r had similar queue length, while 4p5r had slightly shorter queue.

- Recovery blocking operation remains unsure

######################

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
