# Date: 1 Jan 2025
# Link: https://bit.ly/3Pld280
# Name: Largest Element in Array

from typing import List


class Solution:
    def largest(self, arr):
        max = arr[0]
        for i in range(len(arr)):
            max = arr[i] if (max < arr[i]) else max
        return max


obj = Solution()
nums = [1, 8, 7, 56, 90]
# nums = [5, 5, 5, 5]
# nums = [10]
print(obj.largest(nums))
