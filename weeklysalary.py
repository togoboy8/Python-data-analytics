#!/usr/env/python

name = input('What is your name?:  ')

hours = input('How many hours did you work this week?:  ')

hrate = input('Enter your hourly rate?:  ')

ot = int(hours) - 40

otsalary = (int(hrate) *1.5) * int(ot)

weeklysalary = int(hours) * int(hrate)

if int(hours) <= 40:
    print(name + " has worked " +  str(hours) + " hours this week.\n")
    
    print('Great Job for not going overtime!!\n')
    
elif int(hours) > 40:
    
    print(name + " has worked " +  str(hours) + " hours this week.\n")
    
    print("Try not to go overtime!! YOUR ARE MESSING UP WITH THE COMPANY'S MONEY\n")
     
    
    print('Your salary for this week is ' + str(weeklysalary) + ' +  ' + str(ot) + ' extra hours of overtime\n')
    
    weeklysalary += otsalary
    
    print('Anyways, you get to fill up your pocket with an extra $' + str(otsalary) + ' and a total salary of: $' + str(weeklysalary))
    
