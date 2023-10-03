n = int(input())  # arr size
arr = [int(x) for x in input().split()]  # arr input

# pre-compute
hash_size = 13  # size will be given
hash = [0] * hash_size

for i in range(0, n):
    hash[arr[i]] += 1

ans = []
nq = int(input())  # no. of queries
while nq:
    q = int(input())
    ans.append(hash[q])
    nq -= 1

print(ans)
