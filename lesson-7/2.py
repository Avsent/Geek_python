from abc import ABC, abstractmethod

class Clothes(ABC):

    def __init__(self, param):
        self.param = param

    @abstractmethod
    def expend(self):
        pass

class Coat(Clothes):

    @property
    def expend(self):
        return f'fabric consumption for the coats - {self.param * 6.5 + 0.5 :.2f}'

class Suit(Clothes):

    @property
    def expend(self):
        return f'fabric consumption for the suit - {self.param * 2 + 0.3 :.2f}'

c = Coat(200)
s = Suit(100)
print(c.expend)
print(s.expend)
