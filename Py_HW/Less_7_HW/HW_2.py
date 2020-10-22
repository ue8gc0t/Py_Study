from abc import  ABC, abstractmethod


class Clothes:
    @abstractmethod
    def count(self):
        pass


class Coat(Clothes):
    def __init__(self, name, v):
        self.name = name
        self.v = v

    @property
    def count(self):
        return self.v / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self, name, h):
        self.name = name
        self.h = h

    @property
    def count(self):
        return self.h * 2 + 0.3


suit = Suit('qwe', 20)
print(suit.count)
coat = Coat('qwe', 20)
print(coat.count)