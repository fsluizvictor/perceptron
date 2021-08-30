import csv
from typing import List

from src import config


def open_file_csv(file_name: str) -> List[List[str]]:
    with open(file_name, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        file_rows = list()
        for row in spamreader:
            content_row = str(row).split(',')
            file_rows.append(content_row)
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
        value_to_predict = int(str(values[len(values) - 1]).replace('\']', ''))
        values_to_predict.append(str(value_to_predict))
    write_file_csv(config.ABALONE_VALUE_TO_PREDICT_CSV_PATH, values_to_predict)

def read_abalone_values_to_predict()->List[int]:
    rows = open_file_csv(config.ABALONE_VALUE_TO_PREDICT_CSV_PATH)
    return [int(row) for row in rows]
