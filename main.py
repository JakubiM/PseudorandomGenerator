from os import system
from GeneratorLCG import LinearCongruentialGenerator
from Mersenne_Twister import MersenneTwister
from MetodaSrodkaKwadratu import MiddleSquare
from PythonNativeGenerator import PythonNativeGenerator
from Numpy_Mt19937 import NumpyMt19937
from Numpy_PCG64 import NumpyPCG64
from Numpy_Philox import NumpyPhilox
from Numpy_SFC64 import NumpySFC64
from Linear_complexity_test import LinearComplexityTest
from Matrix_Rank_Test import MatrixRankTest

from Image_test import ImageTest
from Spectral_test import SpectralTest


class MyProgram:

    def __init__(self):
        self.listOfGenerators = []

        self.listOfGenerators.append(LinearCongruentialGenerator())
        self.listOfGenerators.append(MersenneTwister())
        self.listOfGenerators.append(MiddleSquare())
        self.listOfGenerators.append(PythonNativeGenerator())
        self.listOfGenerators.append(NumpyMt19937())
        self.listOfGenerators.append(NumpyPCG64())
        self.listOfGenerators.append(NumpyPhilox())
        self.listOfGenerators.append(NumpySFC64())

        self.listOfTests = []

        self.listOfTests.append(ImageTest())
        self.listOfTests.append(SpectralTest())
        self.listOfTests.append(LinearComplexityTest())
        self.listOfTests.append(MatrixRankTest())

    def generators(self):
        system("clear")
        print("Generatory")

    def tests(self):
        system("clear")
        print("testy")

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

    def displayList(self, myList):
        system("clear")
        print("Dostepne opcje:")
        for i in range(len(myList)):
            print("{}. {}".format(i + 1, myList[i].getName()))


program = MyProgram()

system("clear")
print("Wybierz akcje: ")
print("=================")
print("1. Generatory")
print("2. Testy")
print("=================")
choice = program.intInputValid(1, 2)

if choice == 1:
    program.displayList(program.listOfGenerators)
    print("Wybierz generator: ")
    generatorNumber = program.intInputValid(1, 8)
    program.listOfGenerators[generatorNumber - 1].use()
else:
    program.displayList(program.listOfTests)
    print("Wybierz test:")
    testNumber = program.intInputValid(1, 4)
    program.listOfTests[testNumber - 1].use(program.listOfGenerators)
