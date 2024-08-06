from layer import Layer
class NeuralNetwork:
    def __init__(self, learning_rate, input_size, transfer, neuron_sizes):
        self.layers = []

        for i in range(neuron_sizes.shape[0]):
            if i == 0:
                self.layers.append(Layer(input_size, transfer, neuron_sizes[i]))
            else:
                self.layers.append(Layer(neuron_sizes[i-1], transfer, neuron_sizes[i]))
            # burada if ilk katman (giriş k.ı) ise input size kadar noron oluşturuşur amaaaa
            # diğer katmanlarda bir önceki katmanın noron sayısı kadar noron oluşturulmalıııı
            # bu yüzden if else şeklinde kotrol bloğuna ihtiyacımız var

    def train(self, inputs, outputs, epoch, learning_rate):
        for i in range(epoch):
            for k in range(len(self.layers[j].neurons)):
                neuron = self.layers[j].neurons(k)
                print(f'final')