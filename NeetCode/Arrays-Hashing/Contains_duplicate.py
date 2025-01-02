# Date: 2 Jan 2025
# Link: https://leetcode.com/problems/contains-duplicate/
# Name: 217. Contains Duplicate

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashSet = set()
        for i in nums:
            if i in hashSet:
                return True
            hashSet.add(i)
        return False


obj = Solution()
nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
print(obj.containsDuplicate(nums))
