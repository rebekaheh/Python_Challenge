# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 21:50:02 2020

@author: RebekahDSK
"""
# Import to Pandas
import pandas as pd
import csv

# Find the path to the file
# Navigate to the source CSV file
# Shift + Right Click
# Copy as path
# Paste the path after r 
# Name of file = pd.read_csc(r'path of file')
udemy = pd.read_csv(r"C:\Users\RebekahDSK\Desktop\gwu-arl-data-pt-09-2020-u-c\02-Homework\03-Python\01-Mini-Assignment\2.11-HW_UdemyZip\Resources\web_starter.csv")

# Convert contents to a list
content_list = udemy.values.tolist()

# Zip the contents of the list to a single tuple
zip(content_list)

# To show the content that has been zipped
print(content_list)

# Create headers for the columns
udemy.columns = [
    'Course_Id',
    'Course_Title',
    'URL',
    'Is_Paid',
    'Price',
    'Num_Subscribers',
    'Num_Reviews',
    'Num_Published_Lectures',
    'Instructional_Level',
    'Content_Info',
    'Published_Time'
    ]

# Run code, then double click Udemy in Variable Explorer to see changes

# To create a variable that allows you to check the column names you've created
# Run this code then double click the columnName variable in Variable Explorer
columnNames = udemy.columns
                  
# This will export the dataframe (df1) to a CSV file, the path is WHERE YOU WANT IT TO BELOW
# Example, if I want the file to be in my Python_Challenge older, navigate to that folder 
# Right click on desired folder while HOLDING SHIFT and Copy as path
# Paste the path after the r
# And then add this symbol \ at the end before the END QUOTATION MARK and name your csv to whatever you want
# EXAMPLE (example r"C:\Users\JoBigRig\Desktop\ASSSHIT\whatevernameiwant.csv" > 
udemy.to_csv(r"C:\Users\RebekahDSK\Desktop\Python_Challenge\Minis\UdemyZip.csv", encoding = 'utf-8')

##### BONUS

# Find the percent of subscribers that have also left a review on the course
udemy['Percent'] = (udemy['Num_Subscribers'] / udemy['Num_Reviews'].sum()) * 100
# Open Udemny from Variable Explorer and scroll to the right to see the newly added 'Percent' column

# Split text in Content_Info column using the delimiter SPACE
udemy['Content_Info'] = udemy['Content_Info'].str.split(" ", expand = True)[0]

# Export to CSV file again
udemy.to_csv(r"C:\Users\RebekahDSK\Desktop\Python_Challenge\Minis\UdemyZip.csv", encoding = 'utf-8')