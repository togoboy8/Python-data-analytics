# ------------------------------------------------------------------------------
# PYTHONSCRIPT:     collatzSequence.py
# ------------------------------------------------------------------------------
# Project:      collatzSequence
# Created by:   Cedric Hillah on 07/23/2019
# $Last Update: n/a
# $Comment: 
    
	#You are going to develop an application to produce numbers in a sequence. 
	
	# The user will be required to enter a number, and for that number, you will: 
	
	# * Divide the number by 2 if it is even
	
	# * Multiply the number by 3, and add 1 if it is odd. 
	
	# * Do this until you get to 1. 
	
	# Ask the user if he/she would like to input another number, and continue until he/she does not want to enter any more numbers. 
	
	# Show the results as you go. For example, the number 5 should produce the following output: 
	
	# 5 16 8 4 2 1
	
	# The number 3 should produce the following output: 
		
	# 3 10 5 16 8 4 2 1 


# ------------------------------------------------------------------------------



#Prompt user to enter the last number of the range
num = input("Please enter the max number: ")

#Transform user input into an Interger
num = int(num)

print(num)
while (num != 1):
  # #
  #  Divide the number by 2 if it is even
  if (num % 2) == 0:
    num /= 2
    print(int(num))
  #  Multiply the number by 3, and add 1 if it is odd. 
  elif (num % 2) != 0:
    num = (num * 3) +1
    print(int(num))
  # Do this until you get to 1. 
