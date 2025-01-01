#     Parent
#     /   \
#    /     \
# Left    Right
#    \     /
#     \   /
#     Child


class Parent(object):
    def __init__(self):
        super(Parent, self).__init__()
        print("parent __init__()")

    def func(self):
        print("parent func")


class Left(Parent):
    def __init__(self):
        super(Left, self).__init__()
        print("left __init__()")

    def func(self):
        print("Super call left child func")
        super().func()
        print("left func")


class Right(Parent):
    def __init__(self):
        super(Right, self).__init__()
        print("right __init__()")

    def func(self):
        print("Super call within right func")
        super().func()
        print("right func")


class Child(Left, Right):
    def __init__(self):
        super(Child, self).__init__()
        print("child __init__()")

    def func(self):
        print("Super call within child func")
        super().func()
        print("child func")


obj = Child()
print("MRO for super().__init__()-> ", [cls.__name__ for cls in Child.__mro__])

print()

obj2 = Child()
obj2.func()
