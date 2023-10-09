def sequence(n):
    if n <= 0:
        print("Negative number")
    if n == 1:
        return 1
    a, b = 0, 1
    for _ in range(n):
        print(a, end=", ")
        a, b = b, a+b
    print("END")


def sequence_recur(n):
    if n < 0:
        print("Negative number")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return sequence_recur(n-1) + sequence_recur(n-2)


def fib_generator(num):
    a, b = 0, 1
    for _ in range(num):
        yield a
        a, b = b, a + b


sequence(7)
print("\nUsing recursion: ")
for i in range(0, 7):
    print(sequence_recur(i), end=", ")
print("END")
print("\nUsing generator: ")
for i in fib_generator(7):
    print(i, end=", ")
print("END")
