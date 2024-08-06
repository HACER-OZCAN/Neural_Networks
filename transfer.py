from abc import ABC, abstractmethod

class Transfer(ABC):
    @abstractmethod
    def function(self):
        pass

    @abstractmethod
    def derivate(self):
        pass