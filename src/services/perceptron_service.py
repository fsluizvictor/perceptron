import math
from typing import List, Optional

import numpy

from src import config
from src.models.perceptron import Perceptron


class PerceptronService(object):

    def to_train(self, model: Perceptron, x_in: List[int], y: List[int]) -> List[float]:
        bias = [1]
        bias.extend(x_in)

        sum_weighted_entries = list()
        output = list()

        for i in range(len(y)):
            for j in range(len(bias)):
                sum_weighted_entries.append(bias[j] * model.wheights[j][i])
            output.append(self.__sigmoidal(sum_weighted_entries[i]))

        delta_w = numpy.zeros((model.amount_in[0], model.amount_out))

        for i in range(model.amount_in[0]):
            for j in range(model.amount_out - 1):
                delta_w[i][j] = config.LEARNING_COEFFICIENT * (y[j] - output[j] * bias[i])

        for i in range(model.amount_in[0]):
            for j in range(model.amount_out):
                model.wheights[i][j] += delta_w[i][j]

        return output

    def __sigmoidal(self, x: int):
        return 1 / (1 + math.exp(-x))
