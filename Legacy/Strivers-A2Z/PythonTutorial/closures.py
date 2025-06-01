def outer_func(msg):
    message = msg

    def inner_func(name):
        print(message, "->", name)

    return inner_func


x = outer_func('Hi')
x('Abishek')
x('Akshaya')