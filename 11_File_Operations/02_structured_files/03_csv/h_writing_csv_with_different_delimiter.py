#!/usr/bin/python
"""
Purpose: Writing csv using csv module

"""

import csv, pandas as pd
delimiters = {'comma_sep':",", 'space_sep':" ", 'slash_sep':'/'}
for sep in delimiters:
    with open(f"{sep}.csv", "w", newline="") as gh:
        header_names = ("sno", "name", "age", "designation")
        writer = csv.writer(gh, delimiter=delimiters[sep])

        # To write the headers
        writer.writerow(header_names)

        # print(dir(writer))
        writer.writerow([1, "akhila", 11, "carpenter"])
        writer.writerows([[2, "hiral", 12, "software"], [1, "neha", 13, "business"]])
        gh.close()
    data_frame = pd.read_csv(f"{sep}.csv")
    print(f"This is {sep} data")
    print(data_frame.head())
    print()

    # with open(f"{sep}.csv", "r") as file:
    #     csv_reader = csv.reader(file)
    #     # Print each row
    #     for row in csv_reader:
    #         print(row)
# assignment - create csv files with all possible delimiters and read the content also