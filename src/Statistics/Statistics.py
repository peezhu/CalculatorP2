from src.Calculator.Calculator import Calculator
from src.CsvReader.csvReader import CsvReader
from src.Statistics.Mean import mean
from src.Statistics.SampleMean import sample_mean
from src.Statistics.Median import median
from src.Statistics.Mode import mode
from src.Statistics.PopulationVariance import population_variance
from src.Statistics.StandardDeviation import std


class Statistics(Calculator):
    data = []

    def init(self, filepath):
        self.data = CsvReader(filepath)
        super().__init__()

    def mean(self, data):
        self.data = mean(data)
        return self.data

    def sample_mean(self, sample_size):
        self.result = sample_mean(self.data, sample_size)
        return self.result

    def median(self, data):
        self.result = median(data)
        return self.result

    def mode(self, data):
        self.result = mode(data)
        return self.result

    def population_variance(self, data):
        self.result = population_variance(data)
        return self.result

    def std(self, data):
        self.result = std(data)
        return self.result
