# creating a new dictionary
my_dict = {"C++": 100, "Java": 10000, "Python": 112, "C": 1}

v = list(my_dict.values())
k = list(my_dict.keys())
print(k[v.index(max(v))])
print(k[v.index(min(v))])
