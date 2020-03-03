import sys
from os import system
import time
from MyGenerator import MyGenerator


class MersenneTwister(MyGenerator):
    def __init__(self):
        self.seed = 5412321
        self.MT = [0 for x in range(624)]
        self.mti = 0
        self.name = "Mersenne_Twister"
        self.min = 0
        self.max = 999999

    def getFileName(self):
        return "s_{}min_{}max_{}".format(
            str(self.seed),
            str(self.min),
            str(self.max),)

    def setMin(self, min):
        self.min = min

    def setMax(self, b):
        self.b = max

    def setSeed(self, seed):
        self.seed = seed

    def InitMT(self):
        self.MT[0] = self.seed
        for i in range(1, 623):
            x = self.MT[i - 1]
            x = (23023 * x) & 0xFFFFFFFF
            x = (3*x) & 0xFFFFFFFF
            self.MT[i] = x

    def getRandom(self):
        MA = [0, 0x9908B0DF]

        i1 = self.mti + 1
        if i1 > 623:
            i1 = 0

        i397 = self.mti
        if i397 > 623:
            i397 -= 624

        y = (self.MT[self.mti] & 0x80000000) | (self.MT[i1] & 0x7FFFFFFF)
        self.MT[self.mti] = self.MT[i397] ^ (y >> 1) ^ MA[y & 1]
        y = self.MT[self.mti]
        y ^= y >> 11
        y ^= (y << 7) & 0x9D2C5680
        y ^= (y << 15) & 0xEFC60000
        y ^= y >> 18
        self.mti = i1
        return y

    def getRandomFile(self, count):
        self.InitMT()
        res = [(self.min + self.getRandom() % (self.max - self.min + 1))
               for _ in range(count)]
        self.file = open(
            "results/{}/{}".format(self.name, self.getFileName()), 'w+')
        print(res, file=self.file)

    def use(self):
        while True:
            system("clear")
            print("Wybrales {}".format(self.name))
            print(
                "wybierz zmienna ktora chcesz ustawic, \n wartosc w nawiasie jest ustawiona domyslnie")
            print("1. seed          ({})".format(self.seed))
            print("2. min           ({})".format(self.min))
            print("3. max           ({})".format(self.max))
            print("4. Generuj!")
            print("5. Wyjdz!")

            choice = self.intInputValid(1, 8)

            if choice == 1:
                print("Podaj nowy weed: ")
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
                break
