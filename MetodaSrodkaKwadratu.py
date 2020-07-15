from MyGenerator import MyGenerator
from os import system

class MiddleSquare(MyGenerator):

    def __init__(self):
        self.name = "Mid_square_technique"
        self.seed = 0
        self.min = 0
        self.max = 999999

    def getFileName(self, seed):
        return "s_{}min_{}max_{}".format(
            str(seed),
            str(self.min),
            str(self.max))

    def getRandom(self):
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
        self.file = open(
            "results/{}/{}".format(self.name, self.getFileName(seedOnStart)), 'w+')
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
