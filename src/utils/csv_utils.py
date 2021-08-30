import csv
from typing import List

from src import config


def open_file_csv(file_name: str) -> List[List[str]]:
    with open(file_name, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        file_rows = list()
        for row in spamreader:
            file_rows.append(row)
    return file_rows


def write_file_csv(file_name: str, content: List[str]):
    with open(file_name, 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for row in content:
            spamwriter.writerow(row)


def abalone_values_to_predict():
    dataset = open_file_csv(config.ABALONE_CSV_PATH)
    values_to_predict = list()
    for values in dataset:
        print(values[len(values) - 1])
        values_to_predict.append(values[len(values) - 1])
    write_file_csv(config.ABALONE_VALUE_TO_PREDICT_CSV_PATH, values_to_predict)
