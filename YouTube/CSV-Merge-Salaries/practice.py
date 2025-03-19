# practice.py
# merge two csv files 
# source: https://youtu.be/hE3O5hdE3Fs?feature=shared

import csv

# list to store CSV data for new file
new_csv_data = []

# look through the years 2021, 2022, 2023
for year in range(2021, 2024):
    # generate filename dynamically for each year
    filename = f'salaries-{year}.csv'
    
    # open the CSV file for reading
    with open(filename) as csvfile:
        # use DictReader to read CSV file as a dictionary 
        # each row will be a dictionary where keys are column headers, and values are the row data
        reader = csv.DictReader(csvfile)

        # iterate over each row in the file
        for row in reader:
            # append row from csv file to new_csv_data list
            new_csv_data.append(
                [year, # add survey year
                # if the key 'years' is missing, use 'years_of_experience' instead
                row['years_of_experience'] if 'years' not in row else row['years'], # ternary conditional expression
                row['salary']] # add the salary data
            )

# Open a new CSV file to write the combined data
#         file name            write    file type
with open('salaries-full.csv', 'w') as csvfile:
    # create a csv writer object
    writer = csv.writer(csvfile)

    # write the header row (column names)
    writer.writerow([
        'survey_year', 
        'years_of_experience',
        'salary'
    ])

    # write all processed data from new_csv_data
    writer.writerows(new_csv_data)
