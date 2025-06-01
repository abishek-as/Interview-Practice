class Student:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def _displayRollAndBranch(self):
        print("Age: ", self._age)


class Geek(Student):

    def __init__(self, name, age):
        Student.__init__(self, name, age)

    def displayDetails(self):
        print("Name: ", self._name)
        self._displayRollAndBranch()


obj = Geek("R2J", 22)

obj.displayDetails()
print("\nDirect call")
obj._displayRollAndBranch()
