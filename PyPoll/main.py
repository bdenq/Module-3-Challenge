#Dependencies (things needed to run csv function)
import os
import csv

#getting to CSV file and processing it
csvpath = os.path.join("Resources", "election_data.csv")
with open(csvpath) as csvfile:
    #This creates a custom object (data is processed)
    csvreader = csv.reader(csvfile, delimiter =',')
    #skip header
    next(csvreader)

    #creating variables
    total_votes = []
    candidate_names = ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"]
    candidate_votes = [0,0,0]
    percent_candidate_votes = [0,0,0]
    winner = ""

    for row in csvreader:
        #counting votes
        total_votes.append(csvreader)

        #adding candidate votes by going through the list
        for candidate_name_input in candidate_names:
            if (row[2] == candidate_name_input):
                candidate_votes[candidate_names.index(candidate_name_input)] += 1

#Calculating Winner
winner = candidate_names[candidate_votes.index(max(candidate_votes))]
#Calculating Percentage
for person in range(0,len(candidate_votes)):
    percent_candidate_votes[person] = round(candidate_votes[person] / len(total_votes), 3)

#Printing results in terminal
print("Election Results")
print("--------------------------")
print(f"Total Votes: {len(total_votes)}")
print("--------------------------")
for person in range(0,len(candidate_votes)):
    print(f"{candidate_names[person]}: {percent_candidate_votes[person]}% \
         ({candidate_votes[person]})")
print("--------------------------")
print(f"Winner: {winner}")     
print("--------------------------")

#Export files
exportpath = os.path.join("Analysis").replace("\\","/")
with open(exportpath) as exportfile:
    exporttxt = csv.writer(exportfile)
    exporttxt.writerow(["Election Results"])
    exporttxt.writerow(["--------------------------"])
    exporttxt.writerow([f"Total Votes: {len(total_votes)}"])
    exporttxt.writerow(["--------------------------"])
    for person in range(0,len(candidate_votes)):
        exporttxt.writerow([f"{candidate_names[person]}: {percent_candidate_votes[person]}% \
            ({candidate_votes[person]})"])
    exporttxt.writerow(["--------------------------"])
    exporttxt.writerow([f"Winner: {winner}"])
    exporttxt.writerow(["--------------------------"])


