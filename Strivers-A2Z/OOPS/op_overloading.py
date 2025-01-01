# Python Program illustrate how
# to overload an binary + operator
# And how it actually works

class A:
    def __init__(self, a):
        self.a = a

    # adding two objects
    def __add__(self, o):
        return self.a + o.a


ob1 = A(1)
ob2 = A(2)

print(ob1 + ob2)

# Actual working when Binary Operator is used.
print(A.__add__(ob1, ob2))

# And can also be Understand as :
print(ob1.__add__(ob2))
