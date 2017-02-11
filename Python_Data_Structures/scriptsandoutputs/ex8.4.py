## Assignment 8.4

# Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. 
# The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. 
# When the program completes, sort and print the resulting words in alphabetical order.

fname = input("enter a file name:")
path = "C:/Users/SomandLily/Documents/GitHub/Py4e-Coursera/Python_Data_Structures/Data/"
fname = path+fname

try:
	file = open(fname)
except:
	print("file can't open;"+fname)
	exit()
lst = []
for line in file:
	line = line.split()
	for i in range(len(line)):
		if line[i] not in lst :
			lst.append(line[i])
lst.sort()
print(lst)