#!/usr/env/python

# ------------------------------------------------------------------------------
# PYTHONSCRIPT:     StringTypes.py
# ------------------------------------------------------------------------------
# Project:      String Types
# Created by:   Cedric Hillah on 07/24/2019
# $Last Update: n/a
# $Comment:   	Written within the script
  
# ------------------------------------------------------------------------------




x = "blah"
for i in range(1,11):
  print(x)

print()  
print("Another way to do it\n")

x *= 10 

print(x + "\n")

today = "Today is a nice day"

nice = today.split(sep=" ")
print(nice[3] + "\n")

hsname = "Jean Rostand"

hsmascot = "Wildcats"

print("I wen to {} and the mascot was a {}".format(hsname, hsmascot))

print(today.upper())
print()
print(today.lower())
print()
print(today.isalpha())
print()
print(today.find('not'))


print(today.startswith("Today"))

print()

print(today.replace("a nice", "not a nice"))

print()


hi = "Hello World. My name is Cedric Hillah. I am in the Immersive Data Analytics class.".split(sep=".")

print(hi)

print()


too = "     too much white space     "

print(too.rstrip())
print(too.lstrip())
print(too.strip())


lang = "Python", "Java", "PHP", "Javascript", "C++"


favColor = input("Please enter your favorite color")

print(f"My favorite color is {favColor} ")