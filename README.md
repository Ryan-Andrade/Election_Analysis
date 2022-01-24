# Election_Analysis

## Overview of Election Audit
A Colorado Board of Elections employee has given me the following tasks to complete the election audit of a recent local congressional election. 

1. Calculate the total number of votes cast. https://postimg.cc/SnXDq7gQ
2. Get a complete list of candidates who received votes.
3. Get a complete list of the counties who voted in the election.
4. Calculate the total number of votes each candidate received.
5. Calculate the total number of votes cast by each county
6. Calculate the percentage of votes each candidate won. https://postimg.cc/KKSrbXKQ
7. Calculate the percentage of votes cast by each county.
8. Determine the winner of the election based on popular vote.
9. Determine the county with the highest turnout.

## Resources
- Data Source: election_results.csv
- Software: Python 3.8.9, Visual Studio Code, 1.63.2

## Election-Audit Results
The analysis of the election show that: 
- There were "369,711" votes cast in the election.
- The candiates were:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane
- The counties were:
  - Jefferson
  - Denver 
  - Arapahoe  
- The results were:
  -   Charles Casper Stockham received 23.0% of the vote and 85,213 number of votes.
  -   Diana DeGette recieved 73.8% of the vote and 272,892 number of votes.
  -   Raymon Anthony Doane received 3.1% of the vote and 11,606 number of votes.
  - Jefferson county contributing 10.5% of total votes with 38,855
  - Denver county contributing 82.8% of total votes with 306,055
  - Arapahoe county contributing 6.7% of total votes with 24,801  
- The winner of the election was:
  - Diana DeGette who recieved 73.8% of the vote and 272,892 number of votes.

## Election-Audit Summary:
This script can be used for any election with simple modifications. The first modification would be to create a new path for "file_to_load" which will lead users to the new election data. The second would be to generate a new analysis folder by editing the "file_to_save" path. 
