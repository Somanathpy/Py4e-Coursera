## Assignment 7.1

# Write a program that prompts for a file name, then opens that file 
# and reads through the file, and print the contents of the file in upper case. 
# Use the file words.txt to produce the output below.

#hence i saved all the text files in path, i am assigning a path variable, so that i can give only a fine name as input

path = "C:/Users/SomandLily/Documents/GitHub/Py4e-Coursera/Python_Data_Structures/Data/"
fname = input("enter a filename:")

fname = path+fname
file = open(fname)
#print(fname)

for line in file:
	line = line.strip()
	line = line.upper()
	print(line)
