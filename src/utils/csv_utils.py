import csv
from typing import List

from src import config


def open_file_csv(file_name: str) -> List[List[str]]:
    with open(file_name, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        file_rows = list()
        for row in spamreader:
            if row.__contains__(','):
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
        value_to_predict = values[len(values) - 1].replace('\']', '')
        values_to_predict.append(value_to_predict)
    write_file_csv(config.ABALONE_VALUE_TO_PREDICT_CSV_PATH, values_to_predict)


def create_inputs_abalone():
    dataset = open_file_csv(config.ABALONE_CSV_PATH)
    new_dataset = list()
    for values in dataset:
        new_sample = []
        abalone_sex = values[0].replace('[\'', '')
        values.remove(values[0])
        values[len(values) - 1] = str(values[len(values) - 1]).replace('\']', '')
        if abalone_sex == 'M':
            new_sample = ['1', '0', '0']
        if abalone_sex == 'F':
            new_sample = ['0', '1', '0']
        if abalone_sex == 'I':
            new_sample = ['0', '0', '1']
        new_sample.extend(values)
        new_dataset.append(new_sample)
    write_file_csv(config.IN_ABALONE_CSV_PATH, new_dataset)


def read_abalone_dataset(file_name: str = config.IN_ABALONE_CSV_PATH) -> list:
    with open(file_name, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        file_rows = list()
        for row in spamreader:
            row.remove(row[len(row) - 1])
            new_elements = list()
            for element in row:
                if element.isdigit():
                    new_elements.append(int(element))
                else:
                    new_elements.append(float(element))
            file_rows.append(new_elements)
    return file_rows
