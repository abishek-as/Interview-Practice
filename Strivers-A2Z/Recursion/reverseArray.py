def reverseArray_2ptr(a, l, r):
    if l >= r:
        return
    a[l], a[r] = a[r], a[l]
    reverseArray_2ptr(a, l+1, r-1)

def reverseArray_single_var(i, a,n):
    if i>=n/2:return
    

a = [1, 2, 3, 4, 5]
reverseArray_2ptr(a, 0, len(a)-1)
print(a)

a = [1, 2, 3, 4, 5]
reverseArray_single_var(a, 0, len(a)-1)
print(a)
