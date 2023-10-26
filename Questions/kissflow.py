lst = [1, 2, 3, 4, 4, 4, 4, 55, 58, 99, 2, 2, 1, 2, 1, 1, 1, 5, 5, 5, 5]

freq = dict()

# for i in lst:
#     if i in freq:
#         freq[i] += 1
#     else:
#         freq[i] = 1

for i in set(lst):
    freq[i] = lst.count(i)

ans = sorted(freq.items(), key=lambda x: x[1], reverse=True)

n = int(input("Enter n: "))
print(f"Ans: {ans[n-1][0]} -> {ans[n-1][1]}")
