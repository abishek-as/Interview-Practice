s = input()

# pre-compute
hash_size = 256  # size will be given
hash = [0] * hash_size

for i in range(0, len(s)):
    hash[ord(s[i])] += 1

ans = []
nq = int(input())  # no. of queries
while nq:
    q = input()
    ans.append(hash[ord(q)])
    nq -= 1

print(ans)
