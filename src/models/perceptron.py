import numpy

from src import config


class Perceptron(object):

    def __init__(self, amount_in: int, amount_out: int):
        self._amount_in = amount_in,
        self._amount_out = amount_out
        self._wheights = numpy.random.uniform(low=config.MIN_INTERVAL_TO_RANDOMIC_WHEIT,
                                              high=config.MAX_INTERVAL_TO_RANDOMIC_WHEIT,
                                              size=(amount_in, amount_out))

    @property
    def amount_in(self):
        return self._amount_in

    @amount_in.setter
    def amount_in(self, amount_in: int):
        self._amount_in = amount_in

    @property
    def amount_out(self):
        return self._amount_out

    @amount_out.setter
    def amount_out(self, amount_out: int):
        self._amount_out = amount_out

    @property
    def wheights(self):
        return self._wheights
