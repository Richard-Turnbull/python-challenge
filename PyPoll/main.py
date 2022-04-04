#----------------------------------------------------------------------------------------------
# IMPORT MODULES
#----------------------------------------------------------------------------------------------
import os
import csv

#----------------------------------------------------------------------------------------------
# SET VARIABLES
#----------------------------------------------------------------------------------------------
# variable to count the total votes. Set to 0
total_votes = 0
# empty LIST to track a list of unique candidates
list_of_candidates = []
# empty DICTIONARY to track the vote count for each candidate
candidate_vote_count = {}

#----------------------------------------------------------------------------------------------
# READ CSV AND STORE HEADER
#----------------------------------------------------------------------------------------------
poll_data_csv = os.path.join("Resources", "election_data.csv")
with open(poll_data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader, None)

#----------------------------------------------------------------------------------------------
# LOOP THROUGH EACH ROW
#----------------------------------------------------------------------------------------------
    # ForLoop: loop through each row
    for row in csvreader:

        # Add 1 to the vote_count
        total_votes += 1
        
        # Set candidate_name = value in third column of the row
        candidate_name = row[2]

        # Check if candidate in list_of_candidates. If not, add. Set candidate_vote_count to 0
        if candidate_name not in list_of_candidates:
            list_of_candidates.append(candidate_name)
            candidate_vote_count[candidate_name] = 0

        # add +1 to the candidate_vote_count
        candidate_vote_count[candidate_name] += 1

#----------------------------------------------------------------------------------------------
# FIND CANDIDATE WITH MOST VOTES
#----------------------------------------------------------------------------------------------
winning_candidate = max(candidate_vote_count, key=candidate_vote_count.get)

#----------------------------------------------------------------------------------------------
# PRINT TABLE TO TERMINAL
#----------------------------------------------------------------------------------------------
print('________________________________________________________')
print('                                    ')
print('Election Results')
print('--------------------------------------------------------')
print(f'Total Votes: {total_votes}')
print('--------------------------------------------------------')
for c in list_of_candidates:
    candidate_vote_percentage = float(candidate_vote_count[c]) / float(total_votes) * 100
    print(f'{c}: {candidate_vote_percentage:.3f}% ({candidate_vote_count[c]})')
print('--------------------------------------------------------')
print(f'Winner: {winning_candidate}')
print('--------------------------------------------------------')

#----------------------------------------------------------------------------------------------
# WRITE TABLE TO NEW CSV FILE NAMED "OUTPUT"
#----------------------------------------------------------------------------------------------
output_csv = os.path.join("analysis", "output.csv")
with open(output_csv, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write to rows
    csvwriter.writerow(['Election Results'])
    csvwriter.writerow(['--------------------------------------------------------'])
    csvwriter.writerow([f'Total Votes: {total_votes}'])
    csvwriter.writerow(['--------------------------------------------------------'])
    for c in list_of_candidates:
        candidate_vote_percentage = float(candidate_vote_count[c]) / float(total_votes) * 100
        csvwriter.writerow([f'{c}: {candidate_vote_percentage:.3f}% ({candidate_vote_count[c]})'])
    csvwriter.writerow(['--------------------------------------------------------'])
    csvwriter.writerow([f'Winner: {winning_candidate}'])
    csvwriter.writerow(['--------------------------------------------------------'])