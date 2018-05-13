#Import Dependencies

import os
import csv

#Define Variables, set lists

candidates = {} 
total_votes_cast = 0
vote_percentage_candidate = []
number_votes_candidate = []
politicians = []
vote_share_percent = []

#Find File and read file
             
election_csv = os.path.join("raw_data", "election_data_2.csv")
with open(election_csv, newline="") as csvfile:
  csvreader = csv.reader (csvfile, delimiter=",")
  next (csvreader)               
   
#find candidates within the dictionary and add to their respective vote counts

for row in csvreader:       
    if row[2] in candidates:  
      candidates[row[2]] += 1 
    else:                     
      candidates[row[2]] = 1  

#Find total number votes cast

total_votes_cast = csvreader.line_num - 1

for key, value in candidates.items():
    politicians.append(key)
    number_votes_candidate.append(value)  

#find vote percentage per candidate

for x in number_votes_candidate:
    vote_percentage_candidate.append((x/total_votes_cast*100, 1))

#Determine Winner
    
if politicians == max(number_votes_candidate):
    winner = [0]

#prints to file

output_file = os.path.join('Output', 'election_results')

#prints file to terminal
with open(output_file, 'r') as readfile:
    print(readfile.read())


