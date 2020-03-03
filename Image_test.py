import PIL
from PIL import Image, ImageDraw
from pathlib import Path
from MyTest import MyTest
from typing import List
from os import system, listdir
from os.path import isfile


class ImageTest(MyTest):
    def __init__(self):
        self.name = "Image_Test"
        self.size = 1000
        self.min = 0
        self.max = 999999
        self.bgcolor = (255, 255, 255)

    def setList(self):
        with open("./results/{}/{}".format(self.generatorName, self.testedFileName), 'r') as file:
            self.list = eval(file.readline())
        file.close

    def getList(self):
        print(self.list, type(self.list), type(self.list[0]))

    def getName(self):
        return self.name

    def setMax(self, max):
        self.max = max

    def setMin(self, min):
        self.min = min

    def setSize(self, size):
        self.size = size

    def makeDraw(self):

        self.setList()
        image = PIL.Image.new("RGB", (self.size, self.size), self.bgcolor)
        imageD = ImageDraw.Draw(image)

        for i in range(len(self.list)):
            x = self.list[i] % self.size
            y = self.list[i] // self.size
            imageD.line([x, y, x, y], '#000000')

        image.show()
        Path("./results/{}/{}".format(self.generatorName, self.name)
             ).mkdir(parents=True, exist_ok=True)
        image.save("./results/{}/{}/{}.png".format(self.generatorName,
                                                   self.name, self.testedFileName))

    def use(self, listOfGenerators: List[MyTest]):
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
                self.makeDraw()
            else:
                for filename in listdir("./results/{}".format(self.generatorName)):
                    print("Testuje: {}".format(filename))
                    if not isfile("./results/{}/{}".format(self.generatorName, filename)):
                        print("False")
                        continue

                    self.testedFileName = filename
                    self.makeDraw()
# ilosc
# pojedynczych punktow
# histogram od 0 do miliona
