# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 09:37:32 2020

@author: RebekahDSK
"""
# Import Pandas and the CSV
import pandas as pd
import csv

# Read in the CSV file
dframe = pd.read_csv(r"C:\Users\RebekahDSK\Desktop\gwu-arl-data-pt-09-2020-u-c\02-Homework\03-Python\01-Mini-Assignment\3.08-HW_WrestlingWithFunctions\Resources\WWE-Data-2016.csv")

# Prints the first 5 records
#print (dframe.head())

# Prints the last 5 records
#print (dframe.tail())

# %% Define the function and have it accept the 'wrestler_data' as its sole parameter
def print_percentages(wrestler_data):
    
    # For readability, it can help to assign your values to variables with descriptive names
    name = str(wrestler_data[0])
    wins = int(wrestler_data[1])
    losses = int(wrestler_data[2])
    draws = int(wrestler_data[3])

    # Total matches can be found by adding wins, losses, and draws together
    total_matches = wins + losses + draws

    # Win percent can be found by dividing the the total wins by the total matches and multiplying by 100
    win_percent = (wins / total_matches) * 100

    # Loss percent can be found by dividing the total losses by the total matches and multiplying by 100
    loss_percent = (losses / total_matches) * 100

    # Draw percent can be found by dividing the total draws by the total matches and multiplying by 100
    draw_percent = (draws / total_matches) * 100

    # If the loss percentage is over 50, type_of_wrestler is "Jobber". Otherwise it is "Superstar".
    if loss_percent > 50:
        type_of_wrestler = "Jobber"
    else:
        type_of_wrestler = "Superstar"

    # Print out the wrestler's name and their percentage stats
    print(f"Stats for {name}")
    print(f"WIN PERCENT: {win_percent}")
    print(f"LOSS PERCENT: {loss_percent}")
    print(f"DRAW PERCENT: {draw_percent}")
    print(f"{name} is a {type_of_wrestler}")
    
# Prompt the user for what wrestler they would like to search for
name_to_check = input("What wrestler do you want to look for? ")

for index, row in dframe.iterrows():
    if name_to_check == row[0]:
        print_percentages(row)
