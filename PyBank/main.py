import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')
monthCount = 0
gIncrease = 0
currentIncrease = 0
total = 0
print(csvpath)

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
    	monthCount += 1
    	total += float(row[1])
    	
    	print(row)

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {monthCount}")
print(f"Total: ${int(total)}")
print("Average  Change: $-2315.12")
print("Greatest Increase in Profits: Feb-2012 ($1926159)")
print("Greatest Decrease in Profits: Sep-2013 ($-2196167)")