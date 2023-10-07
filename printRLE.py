def printRLE(s):
    encoded = ""
    i = 0
    while i < len(s):
        count = 1
        while i < len(s) - 1 and s[i] == s[i + 1]:
            count += 1
            i += 1
        encoded += s[i] + str(count)
        i += 1
        encoded += s[i] + str(count)
        return encoded


if __name__ == "__main__":
    st = "wwwwaaadexxxxxxywww"
    print(printRLE(st))
