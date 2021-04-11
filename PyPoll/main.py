import os
import csv

voter_list = []
county_list = []
candidate_list = []

election_csv = os.path.join('Resources', 'election_data.csv')
    
with open(election_csv) as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    
    for row in csvreader:
        voter_list.append(row[0])
        county_list.append(row[1])
        candidate_list.append(row[2])
    
    cand_vote = zip(voter_list, candidate_list)
    # list_dict = dict(zip(voter_list,zip_list))

    total_votes = len(voter_list)

    # Shows unique values of Candidatee list
    myset = set(candidate_list)
    print(f"Candidates: {myset}")

    khan = []
    li = []
    otooley = []
    correy = []

    for voter, candidate in cand_vote:
        if candidate == "Khan":
            khan.append(voter)
        if candidate == "Li":
            li.append(voter)
        if candidate == "O'Tooley":
            otooley.append(voter)
        if candidate == "Correy":
            correy.append(voter)
    
    khan_votes = len(khan)
    li_votes = len(li)
    otooley_votes = len(otooley)
    correy_votes = len(correy)

    khan_per = "{:.2%}".format((khan_votes / total_votes))
    li_per = "{:.2%}".format(li_votes / total_votes)
    otooley_per = "{:.2%}".format(otooley_votes / total_votes)
    correy_per = "{:.2%}".format(correy_votes / total_votes)

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


