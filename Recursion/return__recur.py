def fun_param(n, sum):
    if n < 1:
        return sum
    return fun_param(n-1, sum+n)


print(fun_param(5, 0))
