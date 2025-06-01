def square_nums(nums):
    for i in nums:
        yield (i*i)


nums = square_nums([1, 2, 3, 4, 5])
print(nums)
print("Using next keyword:", next(nums))
for i in nums:
    print(i)

nums2 = (i*i for i in [6, 7, 8, 9, 10])
print(nums2)
print("Using next keyword:", next(nums2))
for i in nums2:
    print(i)
