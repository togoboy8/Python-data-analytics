#!/usr/env/python

# ------------------------------------------------------------------------------
# PYTHONSCRIPT:     ElizaApp.py
# ------------------------------------------------------------------------------
# Project:      Eliza Application
# Created by:   Cedric Hillah on 07/24/2019
# $Last Update: n/a
# $Comment:   
  
    # You will be creating an interactive chat-bot type program. Eliza is a therapist program that interacts with the user. Your program will need to evaluate what the user asks and turn the user's input into a question that sounds like the therapist really cares.

    # Your first taskca is to develop a program with a running loop. If the user types in "I am feeling great" or enter "Q", the program will stop running. Your program should print out the last input (as an output) every time before accepting new input. Make sure you are accommodating for NO case-sensitivity. (Q is the same as q)
      

# ------------------------------------------------------------------------------
#keep on asking questions until user enter defined exit input
while True:

  question = "\nGood day. What is your problem? Enter your response here or Q to quit: "
  answer = input(question)
  answer = answer.lower()
  

  #take user input and turn it into lower case then compare with exit variables
  if answer == "q" or answer == "i am feeling great":

      break 
      
    
  else:

    print(answer)
    
    
