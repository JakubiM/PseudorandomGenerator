from MyGenerator import MyGenerator
from numpy.random import Philox, Generator
from pathlib import Path
from os import system


class NumpyPhilox(MyGenerator):

    def __init__(self, *args, **kwargs):
        super(NumpyPhilox, self).__init__(*args, **kwargs)
        self.name = "Numpy_Philox"
        self.seed = 0
        self.min = 0
        self.max = 999999
        self.random = Generator(Philox(self.seed))


    def getRandomFile(self, count):
        self.random = Generator(Philox(self.seed))
        res = [(self.min + self.getRandom() % (self.max - self.min + 1))
               for _ in range(count)]
        self.saveToFile(res)

