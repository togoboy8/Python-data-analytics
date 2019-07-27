# ------------------------------------------------------------------------------
# PYTHONSCRIPT:     FizzBuzz.py
# ------------------------------------------------------------------------------
# Project:      FizzBuzz
# Created by:   Cedric Hillah on 07/24/2019
# $Last Update: n/a
# $Comment:     

    # Write a program that prints the numbers from 1 to 100.

    # For multiples of 3 print “Fizz” instead of the number.

    # For the multiples of five print “Buzz”.

    # For numbers which are multiples of both 3 and 5 print “FizzBuzz”.

# ------------------------------------------------------------------------------

title = "\t\t\tMy first fizzbuzz app"

print()

print(title.upper())


# loop though a range of number from 1 to 100

for i in range(1,100):

# if the number is a multiple of 3 but not of 5 print Fizz

  if (i % 3) == 0 and (i % 5) != 0:
    print("Fizz")

# if the number is a multiple of 5 but not of 3 print Fizz

  elif (i % 3) == 0 and (i % 5) == 0:
    print("FizzBuzz")

# if the number is a multiple of 3 and 5 print Fizz
 
  elif (i % 5) == 0 and (i % 3) != 0:
    print("Buzz")

# else print the number  

  else:
    print(i)