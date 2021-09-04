from MyGenerator import MyGenerator
from os import system
from pathlib import Path


class MiddleSquare(MyGenerator):

    def __init__(self, *args, **kwargs):
        super(MiddleSquare, self).__init__(*args, **kwargs)
        self.name = "Mid_square_technique"
        self.seed = 0
        self.min = 0
        self.max = 999999

    def getRandom(self):
        if self.seed == 0:
            return 0
        lenght = len(str(self.seed))
        center = int(lenght / 2)
        seed = int(self.seed)
        random = seed * seed
        random = str(random)
        random = random.zfill(lenght * 2)
        self.seed = int(random[center:-center])
        return int(random[center:-center])

    def getRandomFile(self, count):
        seedOnStart = self.seed
        res = [(self.min + self.getRandom() % (self.max - self.min + 1))
               for _ in range(count)]
        Path("./results/{}".format(self.name)
             ).mkdir(parents=True, exist_ok=True)
        self.file = open(
            "results/{}/{}".format(self.name, self.getFileName()), 'w+')
        print(res, file=self.file)
