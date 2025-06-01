def CountFrequency(nums):
    freq = {}
    for i in nums:
        freq[i] += 1

        # if i in freq:
        #     freq[i] += 1
        # else:
        #     freq[i] = 1
    print(freq)


# Driver function
if __name__ == "__main__":
    my_list = [1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]

    CountFrequency(my_list)
