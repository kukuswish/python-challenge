import os
import csv
import operator

csvpath = os.path.join('Resources', 'election_data.csv')

totalvotes=0
votes={}

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    # print(csv_header)

    # Read each row of data after the header
    for row in csvreader:
        totalvotes+=1
        key=row[2]
        if row[2] in votes:
            votes[key]+=1
        else:
            votes[key] = 1

winner = max(votes.items(), key=operator.itemgetter(1))[0]

print("Election Results")
print("-------------------------")
print(f"Total Votes: {totalvotes}")
print("-------------------------")
for vote in votes:
    print(f"{vote}: {round(float((votes[vote]/totalvotes)*100),3)}% ({votes[vote]})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

f=open("election_results.txt", 'w')
f.write("-------------------------\n")
f.write(f"Total Votes: {totalvotes}\n")
f.write("-------------------------\n")
for vote in votes:
    f.write(f"{vote}: {round(float((votes[vote]/totalvotes)*100),3)}% ({votes[vote]})\n")
f.write("-------------------------\n")
f.write(f"Winner: {winner}\n")
f.write("-------------------------\n")
f.close()