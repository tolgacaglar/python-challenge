"""
Print a summary of the budget data, reading from csv file
"""

import csv  # The budget data is saved in a csv file
import os   # os.join uses 

# Budget data filepath
filepath = "C:/Users/Tolga/Dropbox/GitHub/python-challenge/PyBank/Resources/budget_data.csv"

# Open the file for read
with open(filepath, mode="r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")  # csv reader with default delimiter ","

    # First line of the file is the header
    csv_header = next(csvreader)

    # Run through each line of the csv file
    count_month = 0     # counting number of months recorded
    max_increase = -1   # greatest increase in profits (>0)
    max_increase_month = ""
    max_decrease = +1   # greatest decrease in profits (<0)
    max_decrease_month = ""
    date_ar = []        # List of recorded Month[3 letter code]-YYYY
    profit_ar = []      # List of recorded profit/loss value at corresponding date
    total = 0    # Total profit/loss
    total_change = 0  # Average change in the profit
    for line in csvreader:
        # Data collection
        date_ar.append(line[0])     # Add the month/year to an array
        profit_ar.append(int(line[1]))       # Profit/loss value for the current month
        
        # Analysis
        total += profit_ar[-1]     # Add the latest added profit value to the total

        if count_month > 0:     # Compare the current data to the previous
            difference = profit_ar[-1] - profit_ar[-2]
            total_change += difference
            # if difference is negative, then there is a decrease.
            if difference < max_decrease:
                max_decrease = difference
                max_decrease_month = line[0]
            # if difference is positive, then there is an increase
            if difference > max_increase:
                max_increase = difference
                max_increase_month = line[0]

        # Increment the number of data by 1
        count_month += 1    #increment the number of month for every added item to an array

    average_profit = total/count_month # Average profit
    average_change = total_change/(count_month-1)    # average change, divide by the (N-1) data


# Print the summary
print("Financial Analysis")
print("---------------")
print("Total Months: %d" % (count_month))
print("Total: $%d" % (total))
print("Average Change: $%.2f" % (average_change))
print("Greatest Increase in Profits: %s ($%d)" % (max_increase_month, max_increase))
print("Greatest Decrease in Profits: %s ($%d)" % (max_decrease_month, max_decrease))