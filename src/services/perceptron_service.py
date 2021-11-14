from datetime import datetime

from src import config
from src.models.datasets.samples import Sample
from src.models.perceptron import Perceptron
from src.services.dataset_service import DataSetService
from src.services.training_service import TrainingService
from src.utils import csv_utils
from src.view.view import View


class PerceptronService:
    def __init__(self):
        pass

    def execute_training(self, sample: Sample, model: Perceptron, view: View, create_csv: bool = False):
        start = datetime.now()
        predict_step = list()
        load_data = DataSetService(sample)
        data = load_data.get_samples()
        dataset_in = data[0]
        dataset_out = data[1]
        for epoch in range(config.EPOCH):
            aproximation_epoch_error = 0
            for s in range(len(sample.x_in())):
                sample_error = 0
                x_in = dataset_in[s]
                y = dataset_out[s]

                outputs = list()
                training = TrainingService(model, x_in, y)
                outputs = training.to_train()

                for i in range(len(outputs)):
                    sample_error = self.__error(y[i], outputs[i])

                aproximation_epoch_error += sample_error
            view.show_divisor()
            predict_step.append(view.show_info_step(epoch, aproximation_epoch_error, sample))
        if create_csv:
            csv_utils.write_file_csv(config.ABALONE_PREDICT_10000_EPOCHS, predict_step)
        end = datetime.now()
        view.show_divisor()
        view.benchmark(end, start)
        view.show_divisor()

    def __error(self, value_wanted: float, value_got: float):
        return abs(value_wanted - value_got)
