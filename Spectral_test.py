from pathlib import Path
from MyTest import MyTest
from typing import List
from os import system, listdir
from os.path import isfile, exists


class SpectralTest(MyTest):
    def __init__(self):
        self.name = "Spectral_Test"
        self.parts = 10
        self.results = [0 for x in range(self.parts)]
        self.max = 1000000

    def getName(self):
        return self.name

    def setList(self):
        with open("./results/{}/{}".format(self.generatorName, self.testedFileName), 'r') as file:
            self.list = eval(file.readline())
        file.close

    def test(self):
        self.setList()
        self.results = [0 for x in range(self.parts)]

        for i in range(len(self.list)):
            self.results[int(self.list[i] // (self.max / self.parts))] += 1

        Path("./results/{}/{}".format(self.generatorName, self.name)
             ).mkdir(parents=True, exist_ok=True)
        file = open("./results/{}/{}/{}".format(self.generatorName,
                                                self.name, self.testedFileName), "w+")

        for i in range(len(self.results)):
            print("{}. {}%".format(i, self.results[i] / float(len(self.list))))
            print("{}. {}%".format(
                i, self.results[i] / float(len(self.list))), file=file)
