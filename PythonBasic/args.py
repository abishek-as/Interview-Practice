def test(*args):
    print(type(args))
    for i in args:
        print(i)


test(1, 2, 3, 4, 5, 6, 7, 7)
