import csv
from typing import List


def open_file_csv(file_name: str) -> List[List[str]]:
    with open(file_name, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        file_rows = list()
        for row in spamreader:
            file_rows.append(row)
    return file_rows
