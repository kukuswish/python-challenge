import os
import csv

#function for increase
def getIncrease(curr,prev):
    increase = curr - prev
    return increase

csvpath = os.path.join('Resources', 'budget_data.csv')

monthCount = 0
gIncrease = 0
gDec = 0
change =0 
currentIncrease = 0
currentMonth = 0
prevMonth = 0
total = 0

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        monthCount += 1
        total = total + float(row[1])

        

        if(monthCount != 0):
            currentMonth= float(row[1])
            change = getIncrease(currentMonth,prevMonth)

            currentIncrease += change
            print(f"{row[0]} {change} {prevMonth} {currentMonth} {currentIncrease}")
            prevMonth=currentMonth   
        else:
            currentIncrease+= float(row[1])
            prevMonth=float(row[1])

        
        if(change >= 0 and change > gIncrease):
            gIncrease= change
            gMonth = row[0]
        
    averIncrease=currentIncrease/(monthCount - 1)
    # print(1170593 - -755566)
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {monthCount}")
print(f"Total: ${int(total)}")
print(f"Average  Change: $-2315.12 {averIncrease}")
print(f"Greatest Increase in Profits: {gMonth} ({int(gIncrease)}) ")
print("Greatest Decrease in Profits: Sep-2013 ($-2196167)")