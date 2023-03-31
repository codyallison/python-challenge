import os
import csv

#sets path for data file
election_csv = os.path.join("Resources", "election_data.csv")

#dictionary to store vote totals
#list to store candidate names

candidateTotals = {}

#initialize total vote counter
totalVotes = 0

#setting winner variables to use later
winner = ""
winCount=0
winPercent=0

#set csvreader w/ delimeter
with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #skip first row
    next(csvreader)

#--------Calculate Election totals--------------

    #for each row add 1 vote to total vote count, and which candidate received it
    for row in csvreader:
        totalVotes +=1
        candidate = row[2]

        #add one vote to individual candidate total
        try:
            candidateTotals[candidate] += 1
        #if keyerror (i.e. Not in the list already) add entry and set to 0
        except KeyError:
            candidateTotals[candidate] = 0


#---------Printing Election Summary---------------------------------------#
    print("Election Results\n-------------------------")
    print(f"Total votes : {totalVotes}\n-------------------------")
    
    #calculates total vote for each candidate and the corresponding percentage of total vote
    for candidate in candidateTotals:
        numCandidateVotes = candidateTotals[candidate]
        percentCandidateVotes = round((numCandidateVotes/totalVotes)*100,3)
        
        #prints candidate summary to console
        print(f"{candidate} : {percentCandidateVotes}% ({numCandidateVotes})\n")

        #if candidate summary is the highest total, their name, total, percentage stored as winner
        if numCandidateVotes > winCount:
            winCount = numCandidateVotes
            winPercent = percentCandidateVotes
            winner = candidate
    print("-------------------------")
    print(f"Winner : {winner}")

#sets path for analysis doc output
output_file = os.path.join("analysis","election_analysis.txt")

#  Open the output file
with open(output_file, "w") as datafile:
    
    #writes election summary to new txt file
    datafile.write("Election Results\n-------------------------\n")
    datafile.write(f"Total votes : {totalVotes}\n-------------------------\n")
    for candidate in candidateTotals:
        datafile.write(f"{candidate} : {percentCandidateVotes}% ({numCandidateVotes})\n")
    datafile.write("-------------------------\n\n")
    datafile.write(f"Winner: {winner}\n\n")
    datafile.write("-------------------------")