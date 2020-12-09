"""
Print a summary of the election results
"""

def print_summary(pout, text):
    if pout is None:
        print(text)
    else:
        pout.write(text)


import csv  # The budget data is saved in a csv file

# Election results filepath
filepath = "PyPoll/Resources/election_data.csv"

# Open the file for read
with open(filepath, mode="r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")  # csv reader with default delimiter ","

    # First line of the file is the header
    csv_header = next(csvreader)

    # Run through each line of the csv file
    total_votes = 0     # counting number of votes recorded
    vote_count = {}   # A dictionary to keep the candidates and their votes
    date_ar = []        # List of recorded Month[3 letter code]-YYYY
    profit_ar = []      # List of recorded profit/loss value at corresponding date
    total = 0    # Total profit/loss
    total_change = 0  # Average change in the profit
    for line in csvreader:
        # Data collection, the file structure is | <ID> | <County> | <Candidate>
        total_votes += 1            # The total number of votes
        candidate = line[2]         # Last column is the candidate
        
        # Count votes for each candidate
        try:
            vote_count[candidate] += 1     # Add 1 point to the existing candidate in the dictionary
        except:
            vote_count[candidate] = 1      # The first time introduction of the candidate to the dictionary

# Text to write for results
text = "Election Results\n"
text += "---------------\n"
text += "Total Votes: %d\n" % (total_votes)
text += "---------------\n"

winner = None   # Initial value of the winner is None
# Run through each candidate to find the winner
for candidate in vote_count.keys():
    if winner is not None:
        if (vote_count[candidate] > vote_count[winner]):    # candidate has a higher vote count
            winner = candidate
    else:
        winner = candidate

    # Print each candidate
    text += "%s: %.3f %% (%d)\n" % (candidate, vote_count[candidate]/total_votes*100, vote_count[candidate])

text += "---------------\n"
text += "Winner: %s\n" % (winner)
text += "---------------\n"

# Print summary to standart output
print_summary(None, text)

# Print summary to a file
with open("PyPoll/analysis/pypoll_analysis.txt", "w") as fout:
    print_summary(fout, text)