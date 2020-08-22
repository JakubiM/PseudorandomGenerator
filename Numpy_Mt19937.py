from MyGenerator import MyGenerator
from numpy.random import MT19937, Generator
from pathlib import Path
from os import system


class NumpyMt19937(MyGenerator):

    def __init__(self, *args, **kwargs):
        super(NumpyMt19937, self).__init__(*args, **kwargs)
        self.name = "Numpy_Mt19937"
        self.seed = 0
        self.min = 0
        self.max = 999999
        self.random = Generator(MT19937(self.seed))

    def getRandomFile(self, count):
        self.random = Generator(MT19937(self.seed))
        res = [(self.min + self.getRandom() % (self.max - self.min + 1))
               for _ in range(count)]
        self.saveToFile(res)

