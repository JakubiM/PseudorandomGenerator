from MyGenerator import MyGenerator
from numpy.random import SFC64, Generator
from pathlib import Path
from os import system


class NumpySFC64(MyGenerator):

    def __init__(self, *args, **kwargs):
        super(NumpySFC64, self).__init__(*args, **kwargs)
        self.name = "Numpy_SFC64"
        self.seed = 0
        self.min = 0
        self.max = 999999
        self.random = Generator(SFC64(self.seed))

    def getRandomFile(self, count):
        self.random = Generator(SFC64(self.seed))
        res = [(self.min + self.getRandom() % (self.max - self.min + 1))
               for _ in range(count)]
        self.saveToFile(res)


