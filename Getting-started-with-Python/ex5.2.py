## Assignment 5.2

# Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. 
# Once 'done' is entered, print out the largest and smallest of the numbers. 
# If the user enters anything other than a valid number catch it with a try/except and put out an appropriate 
# message and ignore the number

largest = None
smallest = None

while True:
	num = input("enter a number:")
	if num == "done":	break
	try:
		num = int(num)
	except:
		print(num+" : is invalid input")
		continue
	largest = num if largest == None or largest < num else largest
	smallest = num if smallest == None or smallest > num else smallest

print("the largest number is :"+ str(largest))
print("the smallest number is :"+str(smallest))