# Date: 1 Jan 2025
# Link: https://leetcode.com/problems/concatenation-of-array/
# Name: 1929. Concatenation of Array

from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums+nums


obj = Solution()
nums = [1, 2, 1]
print(obj.getConcatenation(nums))
