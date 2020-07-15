import random
from datetime import datetime
from os import system


class MyGenerator:

    MAX_SEED_VALUE = 99999999999999999
    MAX_FILE_NUMBER_TO_GENERATE = 10000

    def __init__(self):
        self.name = ""
        self.min = 0
        self.max = 0
        self.seed = 0

    def getName(self):
        return self.name

    def setMin(self, min):
        self.min = min

    def getRandomFile(self, count):
        pass

    def setMax(self, max):
        self.max = max

    def setSeed(self, seed):
        self.seed = seed

    def intInputValid(self, a, b):
        while True:
            try:
                choice = int(input())
            except ValueError:
                choice = a - 1
            if choice < a or choice > b:
                print("Bledny wybor! Sprobuj jeszcze raz")
            else:
                return choice

    def setSeedRangeAndFileCount(self):
        system("clear")
        print("Podaj minimalny seed: ")
        min_seed = self.intInputValid(0, self.MAX_SEED_VALUE)
        print("Podaj maksymalny seed: ")
        max_seed = self.intInputValid(0, self.MAX_SEED_VALUE)
        print("Podaj ilosc plikow do wygenerowania(max 10k): ")
        number_of_files = self.intInputValid(
            1, self.MAX_FILE_NUMBER_TO_GENERATE)
        self.useGeneratorWithRandomSeed(min_seed, max_seed, number_of_files)

    def useGeneratorWithRandomSeed(self, min_seed, max_seed, number_of_files):
        random.seed(datetime.now())
        if min_seed >= max_seed:
            print("Blednie podane zakresy seedu.")
            return
        for i in range(number_of_files):
            random_seed = random.randint(min_seed, max_seed)
            self.setSeed(random_seed)
            self.getRandomFile(1000000)
            system("clear")
            print("Ilosc wygenerowanych plikow: {}".format(i + 1))
