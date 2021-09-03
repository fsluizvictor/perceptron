from datetime import datetime
from typing import List

from src.models.datasets.samples import Sample


class View:
    def __init__(self):
        pass

    def show_info_step(self, epoch: int, error: float, sample: Sample)-> List[str]:
        print('ÉPOCA:', epoch, 'ERRO DE APROXIMAÇÃO:', error, sample)
        return [' ÉPOCA: ', str(epoch), ' ERRO DE APROXIMAÇÃO: ', str(error)]

    def show_divisor(self):
        print('-------------------------------------------------------')

    def benchmark(self, end: datetime, start: datetime):
        print("Took {}m to increase the values".format((end - start).total_seconds() / 60))
