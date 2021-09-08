from src.models.datasets.samples import Sample


class DataSetService(object):
    def __init__(self, sample: Sample):
        self._sample = sample

    def get_samples(self) -> list:
        return [self._sample.x_in(), self._sample.y_out()]
