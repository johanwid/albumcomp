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
* displays data of two opposing albums
* collects which album won the round, sends to controller

controller
* sends round results to model 
* sends album information to view


data storage
* add column to existing data table for wins and losses
* write to csv after each round with album info and results (make easy to parse)
* result csv: for each unique user/session store all previous match ups and add
  to data structure for no repeats
