from abc import ABC, abstractmethod
from typing import List

import numpy
from numpy import ndarray

from src import config
from src.utils import csv_utils


class Sample(ABC):

    def __init__(self):
        pass

    amount_in: int
    amount_out: int

    @abstractmethod
    def x_in(self) -> ndarray:
        pass

    @abstractmethod
    def y_out(self) -> ndarray:
        pass


class And(Sample):
    amount_in = 2
    amount_out = 1

    def x_in(self) -> ndarray:
        return numpy.array([
            [0, 0],
            [0, 1],
            [1, 0],
            [1, 1]
        ])

    def y_out(self) -> ndarray:
        return numpy.array([
            [0],
            [0],
            [0],
            [1]
        ])

    def __str__(self):
        return 'Amostra AND'


class Or(Sample):
    amount_in = 2
    amount_out = 1

    def x_in(self) -> ndarray:
        return numpy.array([
            [0, 0],
            [0, 1],
            [1, 0],
            [1, 1]
        ])

    def y_out(self) -> ndarray:
        return numpy.array([
            [0],
            [1],
            [1],
            [1]
        ])

    def __str__(self):
        return 'Amostra OR'


class Xor(Sample):
    amount_in = 2
    amount_out = 1

    def x_in(self) -> ndarray:
        return numpy.array([
            [0, 0],
            [0, 1],
            [1, 0],
            [1, 1]
        ])

    def y_out(self) -> ndarray:
        return numpy.array([
            [0],
            [1],
            [1],
            [0]
        ])

    def __str__(self):
        return 'Amostra XOR'


class Robot(Sample):
    amount_in = 3
    amount_out = 2

    def x_in(self) -> ndarray:
        return numpy.array([
            [0, 0, 0],
            [0, 0, 1],
            [0, 1, 0],
            [0, 1, 1],
            [1, 0, 0],
            [1, 0, 1],
            [1, 1, 0],
            [1, 1, 1],
        ])

    def y_out(self) -> ndarray:
        return numpy.array([
            [1, 1],
            [0, 1],
            [1, 0],
            [0, 1],
            [1, 0],
            [1, 0],
            [1, 0],
            [1, 0],
        ])

    def __str__(self):
        return 'Amostra ROBOT'


class Abalone(Sample):
    amount_in = 10
    amount_out = 3

    def x_in(self):
        return csv_utils.read_abalone_dataset(config.ABALONE_IN_SELECTED_SAMPLES)

    def y_out(self):
        return csv_utils.read_abalone_dataset(config.ABALONE_OUT_BINARY_REPRESENTATION)

    def __str__(self):
        return 'Amostra ABALONE'
