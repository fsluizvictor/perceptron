import math
from datetime import datetime
from typing import List, Optional

import numpy

from src import config
from src.models.datasets.samples import Sample
from src.models.perceptron import Perceptron
from src.view.view import View


class PerceptronService(object):

    def execute_training(self, sample: Sample, model: Perceptron, view: View):
        start = datetime.now()
        for epoch in range(config.EPOCH):
            aproximation_epoch_error = 0
            for s in range(len(sample.x_in())):
                sample_error = 0
                x_in = sample.x_in()[s]
                y = sample.y_out()[s]

                outputs = list()
                outputs = self.to_train(model, x_in, y)

                for i in range(len(outputs)):
                    sample_error = self.__error(y[i], outputs[i])

                aproximation_epoch_error += sample_error
            view.show_divisor()
            view.show_info_step(epoch, aproximation_epoch_error, sample)
        end = datetime.now()
        view.show_divisor()
        view.benchmark(end, start)
        view.show_divisor()

    def to_train(self, model: Perceptron, x_in: List[int], y: List[int]) -> List[float]:
        x = [1]
        x.extend(x_in)

        u = [0.0] * len(y)
        output = [0.0] * len(y)

        for j in range(len(y)):
            for i in range(len(x)):
                u[j] += (x[i] * model.wheights[i][j])
            output[j] = self.__sigmoidal(u[j])

        delta_w = numpy.zeros((model.amount_in[0] + 1, model.amount_out))

        for j in range(len(u)):
            for i in range(len(x)):
                delta_w[i][j] = config.LEARNING_COEFFICIENT * ((y[j] - output[j]) * x[i])

        for j in range(len(u)):
            for i in range(len(x)):
                model.wheights[i][j] += delta_w[i][j]

        return output

    def __sigmoidal(self, x: float) -> float:
        return 1 / (1 + math.exp(-x))

    def __error(self, value_wanted: float, value_got: float):
        return abs(value_wanted - value_got)
