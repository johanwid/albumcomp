general design ideas

data format:
album ; artist ; year ; rym ; p4k ; fantano ; adjrym ; aggregate ; rep track 

design criteria
* each album is compared one-by-one to every other album
* after a pairing, another randomized pair is presented
*

model
* gets album data, randomizes order
* sends two albums to controller with data
* stores each albums number of wins and losses, or if an album is n/a
* writes results to csv, log each round (which albums and winner)
* use GUIDs for each album?

view
* collects which album won the round, sends to controller

controller
* sends round information to model 
* sends album information to view
