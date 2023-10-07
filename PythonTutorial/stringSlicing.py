arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
start = 0
stop = 10
step = 1

print(arr[start:stop])         # items start through stop-1
print(arr[start:])             # items start through the rest of the array
stop = 7
print(arr[:stop])              # items from the beginning through stop-1
print(arr[:])                  # a copy of the whole array
step = -1
print(arr[start:stop:step])    # start through not past stop, by step
print(arr[::-1])  # reverse the list


# Function to reverse a string
def reverse(string):
    string = "".join(reversed(string))
    return string
 
s = "Geeksforgeeks"
 
print("The original string is : ", end="")
print(s)
 
print("The reversed string(using reversed) is : ", end="")
print(reverse(s))
