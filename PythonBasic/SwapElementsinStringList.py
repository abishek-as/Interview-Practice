test_list = ['Gfg', 'is', 'best', 'for', 'Geeks']

print("The original list is : " + str(test_list))

res = []
for s in test_list:
    new_s = s.replace('G', '-')
    new_s = new_s.replace('e', 'G')
    new_s = new_s.replace('-', 'e')
    res.append(new_s)

print("Modified list: ", str(res))
