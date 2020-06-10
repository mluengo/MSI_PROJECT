#!/usr/bin/python3

# Store data from the interaction files obtained from VMD 
# Timeline tool, summing all the interacions at each time
# frame, at 6 different temperatures in water and vacuum.
# Plot in the X axis the frame and in the Y
# axis the number of interacions

import re
import pylab
dict = {}

list_files_A = ["p3_A_5K.txt", "p3_A_25K.txt" ,"p3_A_50K_bis.txt", "p3_A_100K.txt", "p3_A_150K.txt", "p3_A_200K.txt"] 
list_files_B = ["p3_B_5.txt", "p3_B_25.txt" ,"p3_B_50.txt", "p3_B_100.txt", "p3_B_150.txt", "p3_B_200.txt"] 
colors = ['black', 'blue', 'green', 'yellow',  'orange', 'red']
temps = ['5ºC', '25ºC', '50ºC', '100ºC', '150ºC', '200ºC']
index=0

output = open("p3_AB_totalcontacts.txt","w")

pylab.figure(1, figsize=(10,6))
pylab.xlabel('Frame')
pylab.ylabel('Number of contacts')
#pylab.xlim(0, 51)
#pylab.ylim(70, 280)

for element in list_files_A:
    file = open(element,"r")
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

    # write to file
    for key,value in dict.items():
        output.write("%d %d\n" %(key,value))

    # add line to plot
    pylab.plot(list(dict.values()), color=colors[index], linewidth=2, label=temps[index])
    dict = {}
    index+=1

index=0
dict = {}
for element in list_files_B:
    file = open(element,"r")
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

    # write to file
    for key,value in dict.items():
        output.write("%d %d\n" %(key,value))

    # add line to plot
    pylab.plot(list(dict.values()), color=colors[index], linewidth=2, label=temps[index], dashes=[2, 2])
    dict = {}
    index+=1

# save plot
pylab.grid(True)
pylab.legend()
pylab.savefig("p3_A_B.png", dpi=65)

output.close()