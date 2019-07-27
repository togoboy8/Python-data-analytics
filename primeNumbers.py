#!/usr/env/python

# ------------------------------------------------------------------------------
# PYTHONSCRIPT:     primeNumbers.py
# ------------------------------------------------------------------------------
# Project:      Prime Number
# Created by:   Cedric Hillah on 07/23/2019
# $Last Update: n/a
# $Comment:   
  
	# A prime number is a number that has only itself and 1 as a factor. 
	
	# This means that for each of the numbers from 2 to that number, the number cannot be divided without a remainder. 
	
	# For example, 9 is not a prime number because it can be divided by 3 without a remainder. But 7 is a prime number because it cannot be divided by 2, 3, 4, 5, or 6 without a remainder. 
	
	# Write an appliation that will that show a list of numbers and indicate whether or not they are prime.
	
	# The user will have to input the last number in the range, and you will print all of the numbers from 1 to that number. 
	
	# For example you would have the numbers from 1 to 10 as follow: 
	
	# 1 is not a prime number 
	
	# 2 is a prime number 
	
	# 3 is a prime number 
	
	# 4 is not a prime number
	
	# 5 is a prime number 
	
	# 6 is not a prime number 
	
	# 7 is a prime number 
	
	# 8 is not a prime number 
	
	# 9 is not a prime number 
	
	# 10 is not a prime number 
	

# ------------------------------------------------------------------------------


#Prompt user to enter the last number of the range
num = input("Please enter the max number: ")

#Transform user input into an Interger
num = int(num)
for i in range(1, num):
  if (num % i) == 0:

    print( str(i) + " is NOT a prime number! ")
  else:
    print(str(i) + " is a prime number")