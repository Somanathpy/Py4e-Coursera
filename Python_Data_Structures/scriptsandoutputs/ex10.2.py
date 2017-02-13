## Assignment 10.2

# Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. 
# You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below


import re
fname = input("enter a file name:")
path = "C:/Users/SomandLily/Documents/GitHub/Py4e-Coursera/Python_Data_Structures/Data/"
fname = path+fname
#print(fname)

try:
	file = open(fname)
except:
	print("File not found:"+fname)
	quit()
hours = {}
for line in file:
	line = line.rstrip()
	if not line.startswith('From '): continue
	linesplit = line.split()[5].split(':')
	hours[linesplit[0]] = hours.get(linesplit[0],0) + 1
hourslist = []
for k,v in hours.items():
	hourslist.append((k,v))
hourslist.sort()
for k,v in hourslist:
	print(k,v)

	