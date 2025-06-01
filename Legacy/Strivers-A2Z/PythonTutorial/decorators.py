def add_dec(func):
    def inner(a, b):
        print("I am going to add", a, "and", b)
        return func(a+5, b+5)
    return inner


@add_dec
def divide(a, b):
    print(a + b)


divide(2, 5)

divide(2, 0)
