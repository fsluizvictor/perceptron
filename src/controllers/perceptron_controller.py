import math

from src.models.datasets.samples import Sample
from src.models.perceptron import Perceptron
from src.services.perceptron_service import PerceptronService
from src import config
from src.view.view import View


class PerceptronController(object):

    def __init__(self, sample: Sample):
        self.sample = sample
        self.model = Perceptron(self.sample.amount_in, self.sample.amount_out)
        self.service = PerceptronService()
        self.view = View()

    def execute(self):
        self.service.execute_training(self.sample, self.model, self.view)
