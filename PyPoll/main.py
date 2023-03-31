import os
import csv

#sets path for data file
election_csv = os.path.join("Resources", "election_data.csv")

#store data in separate lists
candidateVotes = []

def get_percent (candidateTotal, electionTotal):
    return round((candidateTotal/electionTotal)*100,3)

def get_candidate_total(candidate):
    return candidateVotes.count(candidate)

#split on comma (make two columns)
with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #skip first row
    next(csvreader)

    #for each row pull who each vote was for and store it to list
    for row in csvreader:
        candidateVotes.append(row[2])
    
    #store each candidate name as a variable
    candidate1 = "Charles Casper Stockham"
    candidate2 = "Diana DeGette"
    candidate3 = "Raymon Anthony Doane"

    #total number of votes
    totalVotes = len(candidateVotes)
    #count vote total and percentages 
    #candidate 1
    candidate1Total = get_candidate_total(candidate1)
    candidate1Percent = get_percent(candidate1Total, totalVotes)
    #candidate 2
    candidate2Total = get_candidate_total(candidate2)
    candidate2Percent = get_percent(candidate2Total, totalVotes)
    #candidate 3
    candidate3Total = get_candidate_total(candidate3)
    candidate3Percent = get_percent(candidate3Total, totalVotes)
    
    #adds candidates and their totals to corresponding lists to find matching index
    voteTotals = [candidate1Total, candidate2Total, candidate3Total]
    candidates = [candidate1, candidate2, candidate3]
    winnerIndex = voteTotals.index(max(voteTotals))
    winner = candidates[winnerIndex]
    
    #printing election analysis summary
    print("Election Results\n-------------------------")
    print(f"Total votes : {totalVotes}\n-------------------------")
    print(f"{candidate1} : {candidate1Percent}% ({candidate1Total})")
    print(f"{candidate2} : {candidate2Percent}% ({candidate2Total})")
    print(f"{candidate3} : {candidate3Percent}% ({candidate3Total})")
    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")

    #sets path for analysis doc output
#output_file = os.path.join("analysis","election_analysis.txt")

#  Open the output file
#with open(output_file, "w") as datafile:
    
    #writes election summary to new txt file
#    datafile.write("Election Results\n-------------------------\n\n")
#    datafile.write(f"Total votes : {totalVotes}\n-------------------------\n\n")
#    datafile.write(f"{candidate1} : {candidate1Percent}% ({candidate1Total})\n\n")
#    datafile.write(f"{candidate2} : {candidate2Percent}% ({candidate2Total})\n\n")
#    datafile.write(f"{candidate3} : {candidate3Percent}% ({candidate3Total})\n\n")
#    datafile.write("-------------------------\n\n")
#    datafile.write(f"Winner: {winner}\n\n")
#    datafile.write("-------------------------")