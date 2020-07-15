from MyGenerator import MyGenerator
from os import system
from os import sys


class LinearCongruentialGenerator(MyGenerator):

    def __init__(self):
        self.name = "Linear_congruential_generator"
        self.seed = 0
        self.m = 4294967296
        self.a = 69069
        self.c = 5
        self.min = 0
        self.max = 999999

    def getFileName(self):
        return "s_{}m_{}a_{}c_{}min_{}max_{}".format(
            str(self.seed),
            str(self.m),
            str(self.a),
            str(self.c),
            str(self.min),
            str(self.max))

    def setM(self, m):
        self.m = m

    def setA(self, a):
        self.a = a

    def setC(self, c):
        self.c = c

    def getRandom(self):
        self.seed = (self.a * self.seed + self.c) % self.m
        return self.seed

    def getRandomFile(self, count):
        res = [(self.min + self.getRandom() % (self.max - self.min + 1))
               for _ in range(count)]
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
            print("2. m             ({})".format(self.m))
            print("3. a             ({})".format(self.a))
            print("4. c             ({})".format(self.c))
            print("5. min           ({})".format(self.min))
            print("6. max           ({})".format(self.max))
            print("7. Generuj jeden!")
            print("8. Generuj masowo z zakresem seedow!")
            print("9. Wyjdz!")

            choice = self.intInputValid(1, 9)

            if choice == 1:
                print("Podaj nowy seed: ")
                self.setSeed(self.intInputValid(0, self.MAX_SEED_VALUE))

            elif choice == 2:
                print("Podaj nowe m: ")
                self.setM(self.intInputValid(0, self.MAX_SEED_VALUE))

            elif choice == 3:
                print("Podaj nowe a: ")
                self.setA(self.intInputValid(0, self.MAX_SEED_VALUE))

            elif choice == 4:
                print("Podaj nowe c: ")
                self.setC(self.intInputValid(0, self.MAX_SEED_VALUE))

            elif choice == 5:
                print("Podaj nowe minimum: ")
                self.setMin(self.intInputValid(0, self.MAX_SEED_VALUE))

            elif choice == 6:
                print("Podaj nowe maksimum: ")
                self.setMax(self.intInputValid(0, self.MAX_SEED_VALUE))

            elif choice == 7:
                self.getRandomFile(1000000)

            elif choice == 8:
                self.setSeedRangeAndFileCount()

            elif choice == 9:
                break
