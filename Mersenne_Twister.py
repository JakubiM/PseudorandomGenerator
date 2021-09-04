import sys
from os import system
import time
from MyGenerator import MyGenerator
from pathlib import Path


class MersenneTwister(MyGenerator):
    def __init__(self, *args, **kwargs):
        super(MersenneTwister, self).__init__(*args, **kwargs)
        self.seed = 5412321
        self.MT = [0 for x in range(624)]
        self.mti = 0
        self.name = "Mersenne_Twister"
        self.min = 0
        self.max = 999999

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
        self.saveToFile(res)
