from abc import ABC, abstractmethod
from typing import List

import numpy
from numpy import ndarray


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


class Or:
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

class Xor:
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

class Robot:
    amount_in = 3
    amount_out = 2

    def x0(self):
        return [0, 0, 0, 0, 1, 1, 1, 1]

    def x1(self):
        return [0, 0, 1, 1, 0, 0, 1, 1]

    def x2(self):
        return [0, 1, 0, 1, 0, 1, 0, 1]

    def y0(self):
        return [1, 0, 1, 0, 1, 1, 1, 1]

    def y1(self):
        return [1, 1, 0, 1, 0, 0, 0, 0]
