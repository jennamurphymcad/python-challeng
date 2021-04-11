import os
import csv

# Empty lists for each column data set
voter_list = []
county_list = []
candidate_list = []

# Link to CSV
election_csv = os.path.join('Resources', 'election_data.csv')

# Open and read through csv
with open(election_csv) as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    
    # Loop through all rows and add data of each column into empty list
    for row in csvreader:
        voter_list.append(row[0])
        county_list.append(row[1])
        candidate_list.append(row[2])
    
    # Candidate and voter lists zipped up into new list
    cand_vote = zip(voter_list, candidate_list)

    # Summary of total votes
    total_votes = len(voter_list)

    # Shows unique values of Candidatee list
    myset = set(candidate_list)
    print(f"Candidates: {myset}")

    # initialize empty lists for each candidate (found by call above) - not sure if this is right :0
    khan = []
    li = []
    otooley = []
    correy = []

    # Add each voter to the empty list for each candidate
    for voter, candidate in cand_vote:
        if candidate == "Khan":
            khan.append(voter)
        if candidate == "Li":
            li.append(voter)
        if candidate == "O'Tooley":
            otooley.append(voter)
        if candidate == "Correy":
            correy.append(voter)
    
    # Count how many votes each candidate received
    khan_votes = len(khan)
    li_votes = len(li)
    otooley_votes = len(otooley)
    correy_votes = len(correy)

    # Calculate and format % of votes
    khan_per = "{:.2%}".format((khan_votes / total_votes))
    li_per = "{:.2%}".format(li_votes / total_votes)
    otooley_per = "{:.2%}".format(otooley_votes / total_votes)
    correy_per = "{:.2%}".format(correy_votes / total_votes)

    # Print to terminal
    print(f"Election Results")
    print(f"_____________________________")
    print(f"Total Votes: {total_votes}")
    print(f"_____________________________")
    print(f"Khan: {khan_per} ({khan_votes})")
    print(f"Correy: {correy_per} ({correy_votes})")
    print(f"Li: {li_per} ({li_votes})")
    print(f"O'Tooley: {otooley_per} ({otooley_votes})")
    print(f"_____________________________")
    print(f"Winner: Khan")
    print(f"_____________________________")

    # Create and write to CSV
    with open('Analysis/results.txt', 'w') as csvfile:
        # Initialize csv.writer
        csvwriter = csv.writer(csvfile, delimiter=' ')

        #Write each line onto new CSV row
        csvwriter.writerow({'Electon Results'})
        csvwriter.writerow({'----------------------------'})
        csvwriter.writerow({f"Total Votes: {total_votes}"})
        csvwriter.writerow({'----------------------------'})
        csvwriter.writerow({f"Khan: {khan_per} ({khan_votes})"})
        csvwriter.writerow({f"Correy: {correy_per} ({correy_votes})"})
        csvwriter.writerow({f"Li: {li_per} ({li_votes})"})
        csvwriter.writerow({f"O'Tooley: {otooley_per} ({otooley_votes})"})
        csvwriter.writerow({'----------------------------'})
        csvwriter.writerow({f"Winner: Khan"})
        csvwriter.writerow({'----------------------------'})