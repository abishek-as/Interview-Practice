class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def _displayAge(self):
        print("Age: ", self.__age)


class Geek(Student):

    def __init__(self, name, age):
        Student.__init__(self, name, age)

    def displayName(self):
        print("Name: ", self.__name)
        self._displayAge()


obj = Geek("R2J", 22)

obj.displayName()
print("\nDirect call")
obj._displayAge()
