from typing import List
from os import system
from os import system, listdir
from os.path import isfile, exists


class MyTest:
    def __init__(self):
        self.name = "MyTest"
        self.generatorName = "MyGenerator"
        self.testedFileName = "MyFile"

    def setGeneratorName(self, generatorName):
        self.generatorName = generatorName

    def setTestedFileName(self, testedFileName):
        self.testedFileName = testedFileName

    def getName(self):
        return self.name

    def get_binary(self, number, fill=20):
        return format(number, 'b').zfill(fill)

    def setList(self):
        with open("./results/{}/{}".format(self.generatorName, self.testedFileName), 'r') as file:
            self.list = eval(file.readline())
        file.close

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

    def test(self):
        pass

    def use(self, listOfGenerators: List):
        while(1):
            system("clear")
            print("Wybrales test: {}".format(self.getName()))
            print("Wybierz generator który chcesz testowac:")
            for i in range(len(listOfGenerators)):
                print("{}. {}".format(i + 1, listOfGenerators[i].getName()))
            choice = self.intInputValid(1, len(listOfGenerators))
            self.setGeneratorName(listOfGenerators[choice - 1].getName())

            system("clear")
            print("Wybierz sposob testowania:")
            print("1. Testuj wybrany plik.")
            print("2. Testuj wszystkie nieprzetestowane pliki generatora {}".format(
                self.generatorName))

            choice = self.intInputValid(1, 2)

            if choice == 1:
                print("Podaj nazwe pliku:")
                self.testedFileName = input()
                self.test()
            else:
                for filename in listdir("./results/{}".format(self.generatorName)):
                    print("Testuje: {}".format(filename))

                    if not isfile("./results/{}/{}".format(self.generatorName, filename)):
                        continue
                    if exists("./results/{}/{}/{}".format(self.generatorName, self.name, filename)):
                        continue
                    self.testedFileName = filename
                    self.test()
