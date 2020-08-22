import random
from datetime import datetime
from os import system
from pathlib import Path


class MyGenerator:

    MAX_SEED_VALUE = 99999999999999999
    MAX_FILE_NUMBER_TO_GENERATE = 10000

    def __init__(self):
        self.name = ""
        self.min = 0
        self.max = 0
        self.seed = 0
        self.numberOfSamples = 500000

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

    def setNumberOfSamples(self, numberOfSamples):
        self.numberOfSamples = numberOfSamples

    def getFileName(self):
        return "s_{}min_{}max_{}".format(
            str(self.seed),
            str(self.min),
            str(self.max))

    def saveToFile(self, res):
        Path("./results/{}".format(self.name)
             ).mkdir(parents=True, exist_ok=True)
        self.file = open(
            "results/{}/{}".format(self.name, self.getFileName()), 'w+')
        print(res, file=self.file)
        print("Wygenerowano prawidlowo!")

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

    
    def getRandom(self):
        return self.random.integers(self.min, self.max + 1)

    def use(self):
        while True:
            system("clear")
            print("Wybrales {}".format(self.name))
            print(
                "wybierz zmienna ktora chcesz ustawic, \n wartosc w nawiasie jest ustawiona domyslnie")
            print("1. seed          ({})".format(self.seed))
            print("2. min           ({})".format(self.min))
            print("3. max           ({})".format(self.max))
            print("4. Generuj jeden!")
            print("5. Generuj masowo z zakresem seedow!")
            print("6. Wyjdz!")

            choice = self.intInputValid(1, 6)

            if choice == 1:
                print("Podaj nowy seed: ")
                self.setSeed(self.intInputValid(0, self.MAX_SEED_VALUE))

            elif choice == 2:
                print("Podaj nowe minimum: ")
                self.setMin(self.intInputValid(0, self.MAX_SEED_VALUE))

            elif choice == 3:
                print("Podaj nowe maksimum: ")
                self.setMax(self.intInputValid(0, self.MAX_SEED_VALUE))

            elif choice == 4:
                self.getRandomFile(self.numberOfSamples)

            elif choice == 5:
                self.setSeedRangeAndFileCount()

            elif choice == 6:
                break
