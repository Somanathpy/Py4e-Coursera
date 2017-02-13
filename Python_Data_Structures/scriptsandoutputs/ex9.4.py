## Assignment 9.4

# Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages. 
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
# After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

fname = input("enter a file name:")
path = "C:/Users/SomandLily/Documents/GitHub/Py4e-Coursera/Python_Data_Structures/Data/"
fname = path+fname
#print(fname)

try:
	file = open(fname)
except:
	print("File not found:"+fname)
	quit()
#linesplit = []
emailers = {}
for line in file:
	line = line.rstrip()
	if line.startswith('From:'):
		line_split = line.split()
		#print(line_split[1])
		emailers[line_split[1]] = emailers.get(line_split[1],0) + 1
#print(linesplit)
#print(emailers)
largest = 0
largest_key = None
for k,v in emailers.items():
	if v > largest:
		largest = v
		largest_key = k
print(str(largest_key)+":::"+str(largest))
		
