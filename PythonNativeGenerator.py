from MyGenerator import MyGenerator
import random
from datetime import datetime
from os import system
from pathlib import Path


class PythonNativeGenerator(MyGenerator):

    def __init__(self):
        self.name = "Python_native_generator"
        self.seed = 0
        self.min = 0
        self.max = 999999
        random.seed(self.seed)

    def getRandom(self):
        return random.randint(self.min, self.max)

    def getFileName(self):
        return "s_{}min_{}max_{}".format(
            str(self.seed),
            str(self.min),
            str(self.max))

    def getRandomFile(self, count):
        random.seed(self.seed)
        res = [(self.min + self.getRandom() % (self.max - self.min + 1))
               for _ in range(count)]
        Path("./results/{}".format(self.name)
             ).mkdir(parents=True, exist_ok=True)
        self.file = open(
            "results/{}/{}".format(self.name, self.getFileName()), 'w+')
        print(res, file=self.file)
        print("Wygenerowano prawidlowo!")

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
                self.getRandomFile(1000000)

            elif choice == 5:
                self.setSeedRangeAndFileCount()

            elif choice == 6:
                break
