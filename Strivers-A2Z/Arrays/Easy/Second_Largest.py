# Date: 2 Jan 2025
# Link: https://bit.ly/3pFvBcN
# Name: Second Largest Element in an Array without sorting

# User function Template for python3
class Solution:
    def getSecondLargest(self, arr):
        n = len(arr)
        if (n < 2):
            return -1
        large = -1
        second_large = -1
        for i in range(n):
            if arr[i] > large:
                second_large = large
                large = arr[i]
            elif arr[i] > second_large and arr[i] != large:
                second_large = arr[i]
        return second_large


obj = Solution()
nums = [12, 35, 1, 10, 34, 1]
print(obj.getSecondLargest(nums))
