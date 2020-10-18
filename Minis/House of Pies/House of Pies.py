# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 19:48:52 2020

@author: RebekahDSK
"""


import pandas as pd

# Opening message followed by presenting the menu to the user
print("Welcome to Rebekah's House of Pies! Here is our list of pies:")        

pie_menu = ('(1) Pecan\n'
            '(2) Apple Crisp\n'
            '(3) Bean\n'
            '(4) Banoffee\n'
            '(5) Black Bun\n'
            '(6) Blueberry Realness\n'
            '(7) Buko\n'
            '(8) Burek\n'
            '(9) Tamale Goodness\n'
            '(10) Steak\n')

# Prints the Pie Menu    
print(pie_menu)

# Create a list to store user input
# Loop through asking the user if they want to buy a pie
# If statements that link the integer with the pie name
L = []
while True:
    user_answer = input("Would you like to order a pie (Yes/No)?: ")
    if (user_answer == 'Yes')|(user_answer == 'yes'):

        pie_number = input("Please choose the pie you'd like to order by entering its corresponding number: ")
        qty_value = input('How many would you like to order? ')
        
        if pie_number == "1":
            pie_name = "Pecan"
            print("Great! We'll have that {}".format(pie_name) + " pie right out for you!")
            dictionaryoforders = {'Pie':int(pie_number),'QTY':str(qty_value),'PieName':str(pie_name)}       
            L.append(dictionaryoforders)
        if pie_number == "2":
            pie_name = "Apple Crisp"
            print("Great! We'll have that {}".format(pie_name) + " pie right out for you!")
            dictionaryoforders = {'Pie':int(pie_number),'QTY':str(qty_value),'PieName':str(pie_name)}       
            L.append(dictionaryoforders)
        if pie_number == "3":
            pie_name = "Bean"
            print("Great! We'll have that {}".format(pie_name) + " pie right out for you!")
            dictionaryoforders = {'Pie':int(pie_number),'QTY':str(qty_value),'PieName':str(pie_name)}       
            L.append(dictionaryoforders)
        if pie_number == "4":
            pie_name = "Banoffee"
            print("Great! We'll have that {}".format(pie_name) + " pie right out for you!")
            dictionaryoforders = {'Pie':int(pie_number),'QTY':str(qty_value),'PieName':str(pie_name)}       
            L.append(dictionaryoforders)
        if pie_number == "5":
            pie_name = "Black Bun"
            print("Great! We'll have that {}".format(pie_name) + " pie right out for you!")
            dictionaryoforders = {'Pie':int(pie_number),'QTY':str(qty_value),'PieName':str(pie_name)}       
            L.append(dictionaryoforders)
        if pie_number == "6":
            pie_name = "Blueberry Realness"
            print("Great! We'll have that {}".format(pie_name) + " pie right out for you!")
            dictionaryoforders = {'Pie':int(pie_number),'QTY':str(qty_value),'PieName':str(pie_name)}       
            L.append(dictionaryoforders)
        if pie_number == "7":
            pie_name = "Buko"
            print("Great! We'll have that {}".format(pie_name) + " pie right out for you!")
            dictionaryoforders = {'Pie':int(pie_number),'QTY':str(qty_value),'PieName':str(pie_name)}       
            L.append(dictionaryoforders)
        if pie_number == "8":
            pie_name = "Burek"
            print("Great! We'll have that {}".format(pie_name) + " pie right out for you!")
            dictionaryoforders = {'Pie':int(pie_number),'QTY':str(qty_value),'PieName':str(pie_name)}       
            L.append(dictionaryoforders)
        if pie_number == "9":
            pie_name = "Tamale Goodness"
            print("Great! We'll have that {}".format(pie_name) + " pie right out for you!")
            dictionaryoforders = {'Pie':int(pie_number),'QTY':str(qty_value),'PieName':str(pie_name)}       
            L.append(dictionaryoforders)
        if pie_number == "10":
            pie_name = "Steak"
            print("Great! We'll have that {}".format(pie_name) + " pie right out for you!")
            dictionaryoforders = {'Pie':int(pie_number),'QTY':str(qty_value),'PieName':str(pie_name)}       
            L.append(dictionaryoforders)
            
    # Once the user says 'no' to ordering, print the following
    else:
        print("Thank you for visiting Rebekah's House of Pies!")
        break
# User input has been kept in a data frame
data = pd.DataFrame(L, columns=['Pie','QTY', 'PieName'])

# After ordering, print a user summary
print(" Here is your order summary:" + " " + data["QTY"].values + " " + data["PieName"].values + " " + "pie(s)")

# print (data)
