import math
from typing import List

import numpy

from src import config
from src.models.perceptron import Perceptron


class TrainingService(object):
    def __init__(self, model: Perceptron, x_in: List[int], y_out: List[int]):
        self._model = model
        self._x_in = x_in
        self._y_out = y_out

    def to_train(self) -> List[float]:
        x = [1]
        x.extend(self._x_in)

        u = [0.0] * len(self._y_out)
        output = [0.0] * len(self._y_out)

        for j in range(len(self._y_out)):
            for i in range(len(x)):
                u[j] += (x[i] * self._model.wheights[i][j])
            output[j] = self.__sigmoidal(u[j])
        delta_w = numpy.zeros((self._model.amount_in[0] + 1, self._model.amount_out))

        for j in range(len(u)):
            for i in range(len(x)):
                delta_w[i][j] = config.LEARNING_COEFFICIENT * ((self._y_out[j] - output[j]) * x[i])

        for j in range(len(u)):
            for i in range(len(x)):
                self._model.wheights[i][j] += delta_w[i][j]

        return output

    def __sigmoidal(self, x: float) -> float:
        return 1 / (1 + math.exp(-x))

    def __error(self, value_wanted: float, value_got: float):
        return abs(value_wanted - value_got)
