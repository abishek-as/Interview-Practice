def printName(n):
    if n == 0:
        return
    print("Abi")
    printName(n-1)


def printName2(i, n):
    if i > n:
        return
    print("Shek")
    printName2(i+1, n)


print("Using no var: ")
printName(5)
print("Using i var: ")
printName2(1, 5)
