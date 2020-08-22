from MyGenerator import MyGenerator
import random
from datetime import datetime
from os import system
from pathlib import Path


class PythonNativeGenerator(MyGenerator):

    def __init__(self, *args, **kwargs):
        super(PythonNativeGenerator, self).__init__(*args, **kwargs)
        self.name = "Python_native_generator"
        self.seed = 0
        self.min = 0
        self.max = 999999
        random.seed(self.seed)

    def getRandom(self):
        return random.randint(self.min, self.max)

    def getRandomFile(self, count):
        random.seed(self.seed)
        res = [(self.min + self.getRandom() % (self.max - self.min + 1))
               for _ in range(count)]
        self.saveToFile(res)

