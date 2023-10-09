# Python example to show the working of multiple
# inheritance

class Base1:
    def __init__(self, n1, n2):
        super().__init__(n2)
        self.str1 = n1
        print("Base1")


class Base2:
    def __init__(self, n2):
        self.str2 = n2
        print("Base2")


class Derived(Base1, Base2):
    def __init__(self, n1, n2):
        super().__init__(n1, n2)
        print("Derived")
        self.printStrs()

    def printStrs(self):
        print(self.str1, self.str2)


ob = Derived("Abi", "Ak")

print("MRO: ", [cls.__name__ for cls in Derived.__mro__])
