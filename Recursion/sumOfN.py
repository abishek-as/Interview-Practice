def fun_param(n, sum):
    if n < 1:
        print(sum, end="")
        return
    fun_param(n-1, sum+n)


def fun_functional(n):
    if n == 0:
        return 0
    return n + fun_functional(n-1)


print("Parametrized call: ", end="")
fun_param(5, 0)
print("\nFunctional call: ", fun_functional(5))
