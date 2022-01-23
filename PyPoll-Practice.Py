# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each canddiate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote. 

# Assign a variable for the file to load and the path.
files_to_load = 'Resources/election_results.csv'

# Open the election results and read the file.

## open() close() method
#election_data = open(file_to_load, r)

## with method
with open(file_to load) as election_data:

# To do: perform analysis.
    print(election_data)

# Close the file.
election_data.close


# Create a filename variable to a direct or indirect path to the file.


# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # Write three counties to the file.
     txt_file.write(
         "Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")
# Close the file.
election_data.close