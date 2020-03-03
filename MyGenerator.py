class MyGenerator:

    MAX_SEED_VALUE = 99999999999999999

    def __init__(self):
        self.name = ""
        self.min = 0
        self.max = 0

    def getName(self):
        return self.name

    def setMin(self, min):
        self.min = min

    def setMax(self, max):
        self.max = max

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

