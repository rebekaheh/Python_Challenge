# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 14:37:45 2020

@author: RebekahDSK
"""

import pandas as pd
import csv

pb_df = pd.read_csv(r"C:\Users\RebekahDSK\Desktop\gwu-arl-data-pt-09-2020-u-c\02-Homework\03-Python\02-Case-Assignment\Solutions\PyBank\Resources\budget_data.csv")

# Total number of months included in the dataset
Months = pb_df["Date"].count()

# Net total amount of Profit/Losses over the entire period
Total_Funds = '${:.0f}'.format(pb_df["Profit/Losses"].sum())


# Change in Profit/Loss from previous month
Average_Change = pb_df["Profit/Losses"].diff()
pb_df["Amount Changed"] = Average_Change

# Max profit
pb_df["Amount Changed"].max()

# Max loss
pb_df["Amount Changed"].min()

# Average Change = Average_Change.sum / Months
Average = (Average_Change).sum() / (Months)

# Greatest increase in profits
Greatest_Increase = '${:.0f}'.format(pb_df["Amount Changed"].max())
grtst_incrs_date = pb_df[pb_df["Date"] == Greatest_Increase]

# Greatest loss 
Biggest_Loss = '${:.0f}'.format(pb_df["Amount Changed"].min())
grtst_loss_date = pb_df[pb_df["Date"] == Biggest_Loss]

print("Total Months: {}".format(Months))
print("Total: {}".format(Total_Funds))
print("Average Change: {}".format(Average))
print("Greatest Increase in Profits: {}".format(Greatest_Increase))
print("Date of Greatest Increase in Profits: {}".format(pb_df.loc[pb_df['Amount Changed'].idxmax(), 'Date']))
print("Greatest Decrease in Profits: {}".format(Biggest_Loss))
print("Date of Greatest Decrease in Profits: {}".format(pb_df.loc[pb_df['Amount Changed'].idxmin(), 'Date']))

pb_df.to_csv(r"C:\Users\RebekahDSK\Desktop\Python_Challenge\Case Assignment\Py_Me_Up_Charlie.csv")

