# Python3 program to implement
# run length encoding
def printRLE(s):
    # Stores output string
    encoded = ""

    i = 0
    while i < len(s):
        # Count occurrences of character at index `i'
        count = 1

        while i < len(s) - 1 and s[i] == s[i + 1]:
            count += 1
            i += 1

        # Append the current character and its count to the result
        encoded += s[i] + str(count)
        i += 1

        encoded += s[i] + str(c)
    return encoded


# Driver code
if __name__ == "__main__":

    st = "wwwwaaadexxxxxxywww"
    print(printRLE(st))
