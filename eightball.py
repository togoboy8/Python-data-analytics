#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
# PYTHONSCRIPT:     eightball.py
# ------------------------------------------------------------------------------
# Project:      Magig 8 Ball
# Created by:   Cedric Hillah on 08/26/2019
# $Last Update: 08/26/2019
# $Comment:  
"""
Create a program that mimics the Magic 8 Ball. 
If you don't know what a Magic 8 Ball is ... 
it's a toy ball containing a clear 'window'. 
You shake the ball and ask it a question. 
A random response rises to the window. 
You can read about the Magic 8 Ball on Wikipedia (Links to an external site).

Your program will prompt the user for a question and select a random answer from the list below. 
See the required output below the responses.

● It is certain
● It is decidedly so
● Without a doubt
● Yes definitely
● You may rely on it
● As I see it, yes
● Most likely
● Outlook good
● Yes
● Signs point to yes
● Reply hazy try again
● Ask again later
● Better not tell you now
● Cannot predict now
● Concentrate and ask again
● Don't count on it
● My reply is no
● My sources say no
● Outlook not so good
● Very doubtful

Implement a loop to continue asking the user for more questions until they enter "No" to stop.

Write a method to handle the generating of the random response.

Display the question and the answer to the user.

YOU ASKED: Will I win the lottery tomorrow?
 
MAGIC 8-BALL SAYS: Reply hazy, try again
 
Do you have another question for the Magic 8-Ball? (y/n)
n

Thank you for playing!



"""


import random 

def response():
    

    list = [" It is certain",
    " It is decidedly so",
    " Without a doubt",
    " Yes definitely",
    " You may rely on it",
    " As I see it, yes",
    " Most likely"," Outlook good",
    " Yes"," Signs point to yes",
    " Reply hazy try again",
    " Ask again later",
    " Better not tell you now",
    " Cannot predict now",
    " Concentrate and ask again",
    " Don't count on it",
    " My reply is no",
    " My sources say no",
    " Outlook not so good",
    " Very doubtful"	]
    question = input("Ask me anything: ")
                     
    while True:
             
        r = random.choice(list)
        r = r.strip()
        print('\njYOU ASKED: ' + question +"\n")
        
        print(f"MAGIC 8-BALL Says: {r}")
        again = input("Do you have another question for Magic 8-BALL? (y/n) ")
        
        if again == 'y':
            input("Ask me another question: ")
            
        else:
            print("\nThank You For Playing!")
            break
response()