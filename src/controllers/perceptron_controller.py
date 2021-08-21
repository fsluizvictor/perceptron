import math

from src.models.datasets.samples import Sample
from src.models.perceptron import Perceptron
from src.services.perceptron_service import PerceptronService
from src import config


class PerceptronController(object):

    def __init__(self, sample: Sample):
        self.sample = sample
        self.model = Perceptron(self.sample.amount_in, self.sample.amount_out)
        self.service = PerceptronService()

    def execute(self):
        for epoch in range(config.EPOCH):
            aproximation_epoch_error = 0
            for s in range(len(self.sample.x_in())):
                sample_error = 0
                x_in = self.sample.x_in()[s]
                y = self.sample.y_out()[s]

                outputs = list()
                outputs = self.service.to_train(self.model, x_in, y)

                for i in range(len(outputs)):
                    sample_error = self.__error(y[i], outputs[i])

                aproximation_epoch_error += sample_error
                print(aproximation_epoch_error)

    def __error(self, value_wanted: float, value_got: float):
        return abs(value_wanted - value_got)
