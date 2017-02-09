#Write a program to prompt the user for hours and rate per hour using raw_input to
# compute gross pay. Award time-and-a-half for the hourly rate for all hours worked
# above 40 hours. Use 45 hours and a rate of 10.50 per hour to test the program 
#(the pay should be 498.75). You should use raw_input to read a string and float() 
#to convert the string to a number. Do not worry about error checking the 
#user input - assume the user types numbers properly.

#python 3.5.2 :: Anaconda 4.1.1 ( 64 bit)

hours = int(input("enter Hours:"))
rate = float(input("enter rate per hour:"))

if hours > 40:
	pay = (hours*rate)+(hours-40)*(0.5*rate)
else:
	pay = hours * rate
print("for hours: "+str(hours)+" the pay is :"+str(pay))
