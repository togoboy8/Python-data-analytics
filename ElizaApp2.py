#!/usr/env/python

# ------------------------------------------------------------------------------
# PYTHONSCRIPT:     ElizaApp2.py
# ------------------------------------------------------------------------------
# Project:      Eliza Application
# Created by:   Cedric Hillah on 07/24/2019
# $Last Update: 07/26/2019
# $Comment:   
  			
# 			You will be creating an interactive chat-bot type program. Eliza is a therapist program that interacts with the user. Your program will need to evaluate what the user asks and turn the user's input into a question that sounds like the therapist really cares.

# Sample hedges:

# Please tell me more
# Many of my patients tell me the same thing
# It is getting late, maybe we had better quit
# Sample qualifiers:

# Why do you say that
# You seem to think that
# So, you are concerned that
# Replacements:

# replace i with you
# replace me with you
# replace my with your
# replace am with are
 

# When the user enters a statement the program responds in one of two ways:

# 1. With a randomly chosen hedge, such as "Please tell me more"

# 2. By changing some keywords  in the user's input string and appending this string to a randomly chosen qualifier. To get a random item from a dictionary, set the dictionary keys to be an index for each qualifier, then select a random number in order to pull the value from the dictionary to get the string qualifier phrase.

 

# Here's how the replacement works:

# The user enters something at the prompt: "my teacher hates me"

# The program will loop through that string and replace "my" with "your" and "me" with "you" and then prepend the qualifier to the replacement string. So, my teacher hates me becomes "Why do you say that your teacher hates you?" The replacement method returns the same words as the user entered only the replacement words have been swapped. Then the qualifier is prepended to the user's words.

# Spend some time thinking how you would search through a string and replacing specific words. Hint: try using the .split() function  			

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

    answer = answer.split()
    for n,i in enumerate(answer):
      if i == 'i':
        answer[n] = 'you'
      if i == 'am':
        answer[n] = 'are'
      if i == 'my':
        answer[n] = 'your'
      if i == 'me':
        answer[n] = 'you'
    
    
    print('\n' + ' '.join(answer) + '?\r')
    
        