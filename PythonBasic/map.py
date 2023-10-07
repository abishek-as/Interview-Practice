l = [1, 2, 3, 4, 5]

l2 = map(lambda x: "even" if x % 2 == 0 else "odd", l)  # returns map object

l2 = list(l2)

print(l2)
