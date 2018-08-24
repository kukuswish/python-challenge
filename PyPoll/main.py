import os
import csv
import operator

csvpath = os.path.join('Resources', 'election_data.csv')

totalvotes=0
khan=0
correy= 0
li=0
otool=0

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(csv_header)

    # Read each row of data after the header
    for row in csvreader:
        totalvotes+=1
        
        if(row[2].upper()=="KHAN"):
            khan+=1
        elif(row[2].upper()=="CORREY"):
            correy+=1
        elif(row[2].upper()=="LI"):
            li+=1
        elif(row[2].upper()=="O'TOOLEY"):
            otool+=1

stats = {'Khan':khan, 'Correy': correy, 'Li': li, "O'Tooley": otool}
winner = max(stats.items(), key=operator.itemgetter(1))[0]

print("Election Results")
print("-------------------------")
print(f"Total Votes: {totalvotes}")
print("-------------------------")
print(f"Khan: {round(float((khan/totalvotes)*100),3)}% ({khan})")
print(f"Correy: {round(float((correy/totalvotes)*100),3)}% ({correy})")
print(f"Li: {round(float((li/totalvotes)*100),3)}% ({li})")
print(f"O'Tooley: {round(float((otool/totalvotes)*100),3)}% ({otool})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")
