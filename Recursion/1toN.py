def fun(i, n):
    if i > n:
        return
    print(i)
    fun(i+1, n)


def fun_backtrack(i, n):
    if i < 1:
        return
    fun_backtrack(i-1, n)
    print(i)


print("Forward approach: ")
fun(1, 5)
print("Backtracking approach: ")
fun_backtrack(5, 5)
