from typing import List
from os import system
import random
from datetime import datetime


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
    
    def useGeneratorWithRandomSeed(self, min_seed, max_seed, number_of_files):
        pass

