def fun(i, n):
    if i < 1:
        return
    print(i)
    fun(i-1, n)


def fun_backtrack(i, n):
    if i > n:
        return
    fun_backtrack(i+1, n)
    print(i)


n = 5
print("Forward approach: ")
fun(n, n)
n = 5
print("Backtracking approach: ")
fun_backtrack(1, n)
