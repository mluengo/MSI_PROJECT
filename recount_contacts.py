#!/usr/bin/python3

# Store data from the interaction file obtained from VMD 
# Timeline tool, summing all the interacions at each time
# frame. Plot in the X axis the frame and in the Y
# axis the number of interacion.

import re
import pylab
dict = {}
inputFile = "p3_A_25K.txt"
outputFile = "p3_A_totalcontacts25.txt"

# store data and sum interactions
file = open(inputFile,"r")
for line in file:
    line = line.strip()
    if re.search("^\d", line):
        nums = line.split(" ")
        num1 = int(nums[0])
        num2 = int(nums[1])
        if num1 not in dict.keys():
            dict[num1] = num2
        elif num1 in dict.keys():
            dict[num1] += num2
    else:
        continue
file.close()

# write time frame and sum of interactions
output = open(outputFile,"w")
for key,value in dict.items():
    output.write("%d %d\n" %(key,value))
output.close()

# plot "frame - number of intercations"
pylab.figure(1, figsize=(10,6))
pylab.ylim(70, 280)
pylab.xlim(0, 51)
pylab.xlabel('Residue position')
pylab.ylabel('Number of contacts')
pylab.plot(list(dict.values()), color='red', linewidth=2, label='200ºC')
pylab.grid(True)
pylab.legend()
pylab.savefig("contactsONE25.png", dpi=65)
