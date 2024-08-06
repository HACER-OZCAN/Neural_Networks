import numpy as np
from neural_network import NeuralNetwork

class Neuron:

    def __init__(self, input_size, transfer):
        self.weight = np.random.randn(input_size, 1)
        self.bias = np.random.randn(1, 1)
        self.transfer = transfer

    # toplama fonkunun modellenmesi
    def sum(self, input):
        return np.dot(input, self.weight) + self.bias

    # transfer fonk modelleme
    def calculate(self, input):
        self.input =input
        self.output = self.transfer.function(self.sum(self.input))
        return self.output  # = fnet

    # agırlıkları güncelleme
    def update(self, input, error, output, learning_rate):
        alpha = NeuralNetwork.learning_rate
        delta = error * self.transfer.derivate(self.output)

        self.weight += alpha * self.input.T.dot(delta)
        self.bias += alpha * delta
