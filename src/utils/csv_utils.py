import csv
from typing import List

from src import config


def open_file_csv(file_name: str) -> List[List[str]]:
    with open(file_name, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        file_rows = list()
        for row in spamreader:
            content_row = row
            if row.__contains__(','):
                content_row = str(row).split(',')
            file_rows.append(content_row)
    return file_rows


def write_file_csv(file_name: str, content: List[str]):
    with open(file_name, 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
        for row in content:
            spamwriter.writerow(row)


def abalone_values_to_predict():
    dataset = open_file_csv(config.ABALONE_CSV_PATH)
    values_to_predict = list()
    for values in dataset:
        value_to_predict = values[len(values) - 1].replace('\']', '')
        values_to_predict.append(value_to_predict)
    write_file_csv(config.ABALONE_VALUE_TO_PREDICT_CSV_PATH, values_to_predict)


def create_inputs_abalone():
    dataset = open_file_csv(config.ABALONE_IN)
    new_dataset = list()
    for values in dataset:
        if 8 <= int(values[len(values) - 1]) <= 10:
            values.remove(values[len(values) - 1])
            new_dataset.append(values)
    write_file_csv(config.ABALONE_IN_SELECTED_SAMPLES, new_dataset)


def create_outputs_abalone():
    dataset = read_abalone_dataset(config.ABALONE_OUT)
    new_dataset = list()
    for value in dataset:
        new_sample = []
        if value[0] == 8:
            new_sample = [1, 0, 0]
        if value[0] == 9:
            new_sample = [0, 1, 0]
        if value[0] == 10:
            new_sample = [0, 0, 1]
        if len(new_sample):
            new_dataset.append(new_sample)
    write_file_csv(config.ABALONE_OUT_BINARY_REPRESENTATION, new_dataset)


def read_abalone_dataset(file_name: str = config.ABALONE_IN_SELECTED_SAMPLES) -> list:
    with open(file_name, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        file_rows = list()
        for row in spamreader:
            if len(row) > 1:
                row.remove(row[len(row) - 1])
            new_elements = list()
            for element in row:
                if element.isdigit():
                    new_elements.append(int(element))
                else:
                    new_elements.append(float(element))
            file_rows.append(new_elements)
    return file_rows
