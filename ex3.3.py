#Write a program to prompt the user for a score using raw_input. Print out a letter 
#grade based on the following table:
#Score Grade
#>= 0.9 A
#>= 0.8 B
#>= 0.7 C
#>= 0.6 D
#< 0.6 F
#If the user enters a value out of range, print a suitable error message and exit. 
#For the test, enter a score of 0.85.

score = float(input("enter a Student score:"))
if score < 0 or score > 1:
	print("Enter score within 0.0 to 1.0 range")
	quit()
if score >= 0.9:
	print("Student Grade is :A")
elif score >= 0.8:
	print("Student Grade is :B")
elif score >= 0.7:
	print("Student Grade is :C")
elif score >= 0.6:
	print("Student Grade is :D")
elif score < 0.6:
	print("Student Grade is :F")

	