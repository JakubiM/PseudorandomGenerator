import PIL
from PIL import Image, ImageDraw
from pathlib import Path
from MyTest import MyTest
from typing import List


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

    def countBlackPixels(self, img):
        image = Image.open(img)
        width, height = image.size
        allPixels = width * height
        blackPixels = 0

        for pixel in image.getdata():
            if pixel == (0, 0, 0):
                blackPixels += 1

        Path("./results/{}/{}".format(self.generatorName, self.name)
             ).mkdir(parents=True, exist_ok=True)
        file = open("./results/{}/{}/{}".format(self.generatorName,
                                                self.name, self.testedFileName + "percentage"), "+w")

        print("Total pixels = {}".format(allPixels), file=file)
        print("Total black pixels = {}".format(blackPixels), file=file)
        coverage = float(blackPixels) / allPixels * 100
        print("Cover with black pixels = {}%".format(coverage), file=file)

    def test(self):

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
        self.countBlackPixels("./results/{}/{}/{}.png".format(self.generatorName,
                                                              self.name, self.testedFileName))
