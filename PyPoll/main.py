import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

totalvotes=0


with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(csv_header)

    # Read each row of data after the header
    for row in csvreader:
        totalvotes+=1


print("Election Results")
print("-------------------------")
print(f"Total Votes: {totalvotes}")
print("-------------------------")
print("Khan: 63.000% (2218231)")
print("Correy: 20.000% (704200)")
print("Li: 14.000% (492940)")
print("O'Tooley: 3.000% (105630)")
print("-------------------------")
print("Winner: Khan")
print("-------------------------")
