from neuron import Neuron
# transfer fonk, noron ve
class Layer:
    def __init__(self, neuron_size, transfer, input_size):
        self.neurons = []
        for _ in range(neuron_size):
            self.neurons.append(Neuron(input_size, transfer))