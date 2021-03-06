# Add our dependencies.
import csv
import os

# Assign a variable to load a file from the path.
file_to_load = os.path.join("Resources/election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# County options.
county_options = []

# County votes.
county_votes = {}

# County with the largest turnout.
largest_turnout = ""
largest_count = 0

# Candidate options.
candidate_options = []

# Candidate votes.
candidate_votes = {}

# Winning Candidate
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:

        # Add to the total vote count.
        total_votes += 1

        # Print the county from each row.
        county_name = row[1]

        # Print the candidate name from each row.
        candidate_name = row[2]

        # If the county does not match any exisiting county...
        if county_name not in county_options:

            # Add it to the list of counties.
            county_options.append(county_name)

            # Begin tracking that county's vote count.
            county_votes[county_name] = 0
        
        # Add a vote to that county's count
        county_votes[county_name] += 1

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:

           # Add it to the list of candidates.
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

# Save the results to the text file.
with open(file_to_save, "w") as txt_file:

    # Print the final vote count to the terminal and save it to the text file.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results)
    txt_file.write(election_results)

    # Print county votes header to the terminal and save it to the text file.
    county_votes_header = ("\nCounty Votes:\n")
    print(county_votes_header)
    txt_file.write(county_votes_header)

    # Iterate through the county list.
    for county in county_votes:

        # Retrieve the vote count of a county.
        votes = county_votes[county]

        # Calculate the percentage of votes:
        vote_percentage = int(votes) / int(total_votes) * 100

        # Print the county results to the terminal and save it to the text file.
        county_results = (f"{county}: {vote_percentage:.1f}% ({votes:,})\n")
        print(county_results)
        txt_file.write(county_results)

        # Determine if the votes is greater than the largest turnout.
        if (votes > largest_count):
            # If true, set largest_turnout = votes...
            largest_count = votes
            # And set the largest_turnout = the county's name.
            largest_turnout = county
    
    # Print the largest turnout summary to the terminal and save it to the text file.
    largest_turnout_summary = (
        f"\n"
        f"-------------------------\n"
        f"Largest County Turnout: {largest_turnout}\n"
        f"-------------------------\n")
    print(largest_turnout_summary)
    txt_file.write(largest_turnout_summary)

    # Iterate trough the candidate list.
    for candidate in candidate_votes:
        
        # Retrieve vote count of a candidate.
        votes = candidate_votes[candidate]

        # Calculate the percentage of votes.
        vote_percentage = int(votes) / int(total_votes) * 100

        # Print the candidate results to the terminal and save it to the text file.
        candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results) 

        # Determine if the votes is greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percentage = vote_percentage...
            winning_count = votes
            winning_percentage = vote_percentage
            # And set the winning_candidate = the candidate's name.
            winning_candidate = candidate
        
    # Print the winning candidate summary to the terminal and save it to the text file.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n" 
        f"-------------------------")
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)