## Assignment 8.5

# Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line:
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message). 
# Then print out a count at the end.
# Hint: make sure not to include the lines that start with 'From:'.

fname = input("enter a file name:")
path = "C:/Users/SomandLily/Documents/GitHub/Py4e-Coursera/Python_Data_Structures/Data/"
fname = path+fname
#print(fname)

try:
	file = open(fname)
except:
	print("File not found:"+fname)
	quit()
linesplit = []
for line in file:
	line = line.rstrip()
	if line.startswith('From:'):
		linesplit = line.split()
		print(linesplit[1])
		
