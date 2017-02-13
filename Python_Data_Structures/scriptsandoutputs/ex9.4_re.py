## Assignment 9.4 using regular expressions

# Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages. 
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
# After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

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
emailers = {}
for line in file:
	if line.startswith('From:'):
		m = re.search(r'([A-Za-z0-9-._]+@[A-Za-z0-9-._]+)',line)
		if m:
			email = m.group(0)
			if email in emailers:
				emailers[email] += 1
			else:
				emailers[email] = 1
#print(emailers)
largest_count = 0
largest_key = None

for k,v in emailers.items():
	if v > largest_count:
		largest_count = v
		largest_key = k
print(largest_key,largest_count)
		