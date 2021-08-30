from src.controllers.perceptron_controller import PerceptronController
from src.models.datasets.samples import And, Or, Xor, Robot
from src.utils import csv_utils


class PerceptronRunner:

    def __init__(self):
        and_sample = And()
        or_sample = Or()
        xor_sample = Xor()
        robot_sample = Robot()
        #self.perceptron_controller = PerceptronController(and_sample)
        #self.perceptron_controller = PerceptronController(or_sample)
        #self.perceptron_controller = PerceptronController(xor_sample)
        #self.perceptron_controller = PerceptronController(robot_sample)
        csv_utils.abalone_values_to_predict()

    def runner(self):
        self.perceptron_controller.execute()
