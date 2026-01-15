class X:
    def __init__(self):
        self.__variable = 5
    def print(self):
        print(self.__variable)

class Y(X):
    def __init__(self):
        super().__init__()
        self._X__variable = 6

x = Y()
x.print()
print(x._X__variable)