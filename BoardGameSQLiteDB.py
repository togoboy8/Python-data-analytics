#!/usr/bin/env python
# coding: utf-8

# In[74]:


#!/usr/env/python

# ------------------------------------------------------------------------------
# PYTHONSCRIPT:     BGameSQLDB.py
# ------------------------------------------------------------------------------
# Project:      Board_Game_SQLite_DB
# Created by:   Cedric Hillah on 08/09/2019
# $Last Update: 08/9/2019
# $Comment:  
#
# Download the Board Games SQLite database (Links to an external site.) from Kaggle. 
# Then in Jupyter Notebook, read in the data for each table. 
# Use code to show the number of rows and columns for each table in the database. 
#  ------------------------------------------------------------------------------


# In[75]:


#library to connect & interact with databases
from sqlalchemy import create_engine, inspect
#import pandas to convert list to data frame
import pandas as pd


# In[76]:


#set the database file location to a variable
db = r'C:\Users\GBTC408010ur\Downloads\board-games-dataset\database.sqlite'


# In[77]:


# set the connection to SQLite database in a variable
engine = create_engine(f"sqlite:///{db}")


# In[78]:


#get a list of all the tables in the database
tnames = engine.table_names()



# In[79]:


#check if a table exists
#engine.has_table('BoardGames')


# In[80]:


#this is used to look at the schema of elements in a database
inspector = inspect(engine)


# In[81]:


# get the fields (columns) and their attributes for the table called "bgg.topics"
#this is a list where each item is a field(column)

print(inspector.get_columns('BoardGames'))


# In[82]:


#set the table column information to a variable
fields = inspector.get_columns('BoardGames')


# In[83]:


#put the information into a dataframe for readability
fields_name = pd.DataFrame.from_dict(fields)
#fields_name


# In[84]:



rows = fields_name.count()
#rows[0]


# In[85]:


col = len(fields_name.columns)


# In[86]:


print(f'This Board Game has {rows[0]} rows and {col} columns')


# In[ ]:





# In[92]:


# adding color
PURPLE = '\033[95m'
CYAN = '\033[96m'
DARKCYAN = '\033[36m'
BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
END = '\033[0m'


# In[98]:


# Putting everything together
# Use code to show the number of rows and columns for each table in the database.


for tname in tnames:    
    print(tname)
    fields = inspector.get_columns(tname)
    fields_name = pd.DataFrame.from_dict(fields)
    rows = fields_name.count()
    col = len(fields_name.columns)
    print("\n")
    print(f'This Board Game has {BLUE}{rows[0]}{END} rows and {BLUE}{col}{END} columns')
    print("-----------------------------------------\n")


# In[ ]:





# In[ ]:




