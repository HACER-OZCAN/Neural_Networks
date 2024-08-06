"""import numpy as np
import pandas as pd
from transfer import Transfer

class Sigmoid(Transfer):

    def calculate(self, x):
        return 1 / (1 + np.exp(-x))

    def derivate(self, x):
        return self.calculate(x) * (1 - sigmoid(x))"""
import numpy as np
from neural_network import NeuralNetwork
from sigmoid import Sigmoid
from neuron import Neuron
from data import Data

if __name__ == '__main__':
    sigmoid = Sigmoid()
    model = NeuralNetwork(0.1)
    size = 5

    neuron = Neuron(size, sigmoid)
    input = np.random.randn(size)
    output = neuron.calculate(input)

    model = NeuralNetwork(data.input_size)
    print(f'final')



