def bS(arr, target):
    low, high = 0, len(arr) - 1
    while low < high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        else:
            if target > arr[mid]:
                low = mid + 1
            else:
                high = mid - 1
    return -1


def bS_Rec(arr, low, high, target):
    if low > high:
        return -1
    mid = (low+high)//2
    if arr[mid] == target:
        return mid
    else:
        if target > mid:
            return bS_Rec(arr, mid + 1, high, target)  # Split right
    return bS_Rec(arr, low, mid - 1, target)  # Split Left


arr = [1, 2, 3, 4, 5]
x = 1
ans = bS(arr, x)
print(x, "found at ->", ans) if ans != -1 else print(x, "Not found")
x = 10
ans = bS(arr, x)
print(x, "found at ->", ans) if ans != -1 else print(x, "Not found")

x = 1
ans = bS_Rec(arr, 0, len(arr)-1, x)
print(x, "(Recursive) found at ->", ans) if ans != - \
    1 else print(x, "Not (Recursive) found")
x = 10
ans = bS_Rec(arr, 0, len(arr)-1, x)
print(x, "(Recursive) found at ->", ans) if ans != - \
    1 else print(x, "Not (Recursive) found")
