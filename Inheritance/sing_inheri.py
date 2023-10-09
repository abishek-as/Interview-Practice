class A:
    def __init__(self) -> None:
        print("Class A called")

    def func(self):
        print("Class A func")


class C:
    def func(self):
        print("Class C func")


class B(A):
    def __init__(self) -> None:
        super().__init__()
        print("Class B called")

        print("\nsuper().func() call")
        super().func()  # Calling base class method

        print("\nself.func() call")
        self.func()  # Calling same class method

        print("\nA.func(self) call")
        A.func(self)  # Calling any class method

        print("\nC.func(self) call")
        C.func(self)  # Calling any class method

    def func(self):
        print("Class B func")
        super().func()


Obj = B()
Obj.func()
print(B.__mro__)
