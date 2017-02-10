## Assignment 7.2

# Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines and compute the average of those values and 
# produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
# when you are testing enter mbox-short.txt as the file name.

import string

fname = input("enter file name:")
path = "C:/Users/SomandLily/Documents/GitHub/Py4e-Coursera/Python_Data_Structures/Data/"
fname = path+fname
try:
	file = open(fname)
except:
	print("can't open file: "+fname)
total = 0
count = 0
for line in file:
	if line.startswith('X-DSPAM-Confidence:'):
		m = len(line)
		pos = line.find(':')
		num = float(line[pos+1:m])
		total += num
		count += 1
print("Total :"+str(total))
print("count :"+str(count))
print("average: "+str(total/count))

		
	
