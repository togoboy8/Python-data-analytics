#!/usr/env/python3

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

#library to connect & interact with databases
from sqlalchemy import create_engine, inspect
#import pandas to convert list to data frame
import pandas as pd


#set the database file location to a variable
db = r'C:\Users\GBTC408010ur\Downloads\board-games-dataset\database.sqlite'
# set the connection to SQLite database in a variable
engine = create_engine(f"sqlite:///{db}")
#get a list of all the tables in the database
tnames = engine.table_names()
inspector = inspect(engine)

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