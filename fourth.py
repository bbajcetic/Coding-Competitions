import sys
import re
import math
from math import floor

lines = [line.strip() for line in sys.stdin.readlines()]
line1 = [int(i) for i in re.split("[^0-9]", lines[0])]
questions = [[int(i) for i in re.split("[^0-9]", j)] for j in lines[1:]]
#line1 is list of [octopuses, watches per octopus]
#questions is list of list, [octopus i][watch i]

#print (line1)
#print (questions)

#2 options: add hour to all watches of 1 octopus (max 8)
# or add an hour to a specific watch for all the octopuses
maxwatches = 0
watches = 0
for i in range(0,line1[0]): #number of octopuses
    for j in range(0,line1[1]): #number of watches
        if questions[i][j]%3 == 2:
            watches+=1
    #print("Octopus ",i,"= ",watches," watches")
    if watches > maxwatches:
        maxwatches = watches
    watches = 0
for i in range(0,line1[1]): #number of watches
    for j in range(0,line1[0]): #number of octopuses
        if questions[i][j]%3 == 2:
            watches+=1
    #print("Watch ",i,"= ",watches," octopuses")
    if watches > maxwatches:
        maxwatches = watches
    watches = 0
print (maxwatches)
