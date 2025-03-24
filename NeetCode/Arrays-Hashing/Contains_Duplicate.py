# Date: 2 Jan 2025
# Link: https://leetcode.com/problems/contains-duplicate/
# Name: 217. Contains Duplicate

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # ✅ Approach 1: Using a set to track seen elements
        hashSet = set()  # Create an empty set to store unique elements

        for i in nums:  # Loop through each element in nums
            if i in hashSet:  # Check if the element already exists in the set
                return True  # Return True if a duplicate is found
            hashSet.add(i)  # Add the element to the set if it's not already present

        # If no duplicates are found after looping through the array
        return False

    def containsDuplicateAlt(self, nums: List[int]) -> bool:
        # ✅ Approach 2: Using set conversion and length comparison
        # Convert nums to a set (removes duplicates) and compare lengths
        return len(nums) != len(
            set(nums)
        )  # Return True if lengths differ (duplicates exist)


obj = Solution()
nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
# print(obj.containsDuplicate(nums))
print(obj.alternateApproach(nums))
