from src.models.datasets.samples import Sample


class View:
    def __init__(self):
        pass

    def show_info_step(self, epoch: int, error: float, sample: Sample):
        print('ÉPOCA:', epoch, 'ERRO DE APROXIMAÇÃO:', error, sample)

    def show_divisor(self):
        print('-------------------------------------------------------')


