from MyTest import MyTest
import NISTtests
from os import system
from os import system, listdir
from os.path import isfile, exists
from pathlib import Path
from typing import List


class MatrixRankTest(MyTest):

    def __init__(self):
        self.name = "Matrix_rank_test"
        self.tester = NISTtests.RandomnessTester(None)
        self.bitCount = 32
        self.bitStringSize = 1000

    def test(self):
        self.setList()
        bitstring = ""

        for i in range(32):
            bitstring += self.get_binary(self.list[i], self.bitCount)
        p_value_matrix = self.tester.matrix_rank(bitstring, 32)

        Path("./results/{}/{}".format(self.generatorName, self.name)
             ).mkdir(parents=True, exist_ok=True)
        file = open("./results/{}/{}/{}".format(self.generatorName,
                                                self.name, self.testedFileName), "w+")

        print("Binary matrix rank test p_value: {}.".format(p_value_matrix))
        print("Binary matrix rank test p_value: {}.".format(
            p_value_matrix), file=file)

