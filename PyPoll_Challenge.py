# -*- coding: UTF-8 -*-
"""PyPoll Homework Challenge Solution."""

# Add our dependencies.
import csv
from itertools import count
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Initialize a total vote counter.

#Goal:
    #voter turnout of each county
    #percentage of voters from each county out of the total counts
    #county with the highest turnout*.

#deliverable 1 - election results printed to the command line*
#deliver 2 - election results saved to a text file*
#deliverable 3 - written analysis of the elction audit readme files*.

# Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}

# 1: Create a county list and county votes dictionary.
#initializing county list*.
county_list = []
#initliainzg a dictionary for county list name and votes cast*.
county_dict = {}

#2 initializing outcome variables**.
#initializing empty string for winner county by turnout*.
highest_county_name = ""
#initializing winng count variable for county with most turnout*.
highest_turnout_count= 0
highest_turnout_percentage=0
#initializing total votes by county variable*.
total_votes=0

# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as county_election_data:
    reader = csv.reader(county_election_data)
    # Read the header
    header = next(reader)
    print(header)
    #4a - writing decisoin statement to check if county name is in county list*.
    for row in reader:
        # Add to the total vote count
        total_votes = total_votes + 1
        # Get the county name from each row.
        candidate_name = row[2]
        #extracting data by county*.
        county_name = row[1]
            # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1
        # 4b: Add the  county to the list of counties.
        if county_name not in county_list:
            # Add the county name to the county list.
            county_list.append(county_name)
            # 4c -  begin tracking votes (determined as each row) in dictionary with county names*.
            county_dict[county_name] = 0
        # 5 add county's vote count as looping through rows*.
        county_dict[county_name] += 1
        #6a - repetition statement getting county from county dictionary.

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")
    txt_file.write(election_results)

    for county_name in county_dict:
        #6b - creating votes variable to hold county votes as retrieved from dict*.
        votes = county_dict.get(county_name)
        #6c - script to calculate county votes as percentage of total votes*.
        vote_percentage = float(votes) / float(total_votes) * 100
        county_outcomes = (
        #6d - printing statement to terminal on county vote outputs***.
        f"{county_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(county_outcomes)
        #6e - write data to output files**.
        txt_file.write(county_outcomes)
        #6f - decision statement determining county with largest vote countes and adding its vote counts variables made in Step2*.
        # Determine winning vote count, winning percentage, and candidate.
        if (votes > highest_turnout_count) and (vote_percentage > highest_turnout_percentage):
            highest_turnout_count = votes
            highest_county_name = county_name
            highest_turnout_percentage = vote_percentage
        # 7Print the winning candidate (to terminal)
    highest_county_summary = (
        f"-------------------------\n"
        f"Largest County Turnout: {highest_county_name}\n"
        f"-------------------------\n")
    txt_file.write(highest_county_summary)

    # Save the final candidate vote count to the text file.
    for candidate_name in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the
        # terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)


