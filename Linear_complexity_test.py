from MyTest import MyTest
import NISTtests
from os import system
from os import system, listdir
from os.path import isfile, exists
from pathlib import Path
from typing import List


class LinearComplexityTest(MyTest):

    def __init__(self):
        self.name = "Linear_complexity_test"
        self.tester = NISTtests.RandomnessTester(None)
        self.blockSize = 500
        self.bitCount = 32
        self.bitStringSize = 1000

    def test(self):
        self.setList()
        bitstring = ""

        for i in range(self.bitStringSize):
            bitstring += self.get_binary(self.list[i], self.bitCount)

        p_value = self.tester.linear_complexity(bitstring, self.blockSize)

        if p_value > 0.01:
            result = "pass"
        else:
            result = "fail"

        Path("./results/{}/{}".format(self.generatorName, self.name)
             ).mkdir(parents=True, exist_ok=True)
        file = open("./results/{}/{}/{}".format(self.generatorName,
                                                self.name, self.testedFileName), "w+")

        print("Test result: {} with p_value: {}.".format(result, p_value))
        print("Test result: {} with p_value: {}.".format(
            result, p_value), file=file)

