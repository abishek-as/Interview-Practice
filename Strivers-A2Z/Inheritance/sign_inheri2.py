class A:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Class A: ", self.name, self.age)

    def __str__(self):
        return f"Inside __str__ of Class A: {self.name}, {self.age}"


class B(A):
    def __init__(self, name, age, marks):
        super().__init__(name, age)
        self.marks = marks

    def display(self):
        super().display()
        print("Class B: ", self.marks)

    def __str__(self):
        return f"Inside __str__ of Class B: {self.marks}"


obj1 = A("Ak", "23")
print(obj1)
obj2 = B("Abi", 18, 99)
obj2.display()
print(obj2)
