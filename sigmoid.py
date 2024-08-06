import numpy as np
import andas as pd
from transfer import Transfer

class Sigmoid(Transfer):

    def calculate(self, x):
        return 1 / (1 + np.exp(-x))

    def derivate(self, x):
        return self.calculate(x) * (1 - self.calculate(x))