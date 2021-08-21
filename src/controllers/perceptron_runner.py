from src.controllers.perceptron_controller import PerceptronController
from src.models.datasets.samples import And


class PerceptronRunner:

    def __init__(self):
        and_sample = And()
        self.perceptron_controller = PerceptronController(and_sample)

    def runner(self):
        self.perceptron_controller.execute()
