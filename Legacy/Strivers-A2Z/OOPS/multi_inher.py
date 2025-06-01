# Python example to show the working of multiple
# inheritance

class Base1:
    def __init__(self):
        self.str1 = "Geek1"
        print("Base1: ", id(self))


class Base2:
    def __init__(self):
        self.str2 = "Geek2"
        print("Base2: ", id(self))


class Derived(Base1, Base2):
    def __init__(self):

        # Calling constructors of Base1
        # and Base2 classes
        Base1.__init__(self)
        Base2.__init__(self)
        print("Derived: ", id(self))

    def printStrs(self):
        print(self.str1, self.str2)


ob = Derived()
ob.printStrs()
