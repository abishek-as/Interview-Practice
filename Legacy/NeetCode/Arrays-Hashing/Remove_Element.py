# Date: 26 March 2025
# Link: https://leetcode.com/problems/remove-element/
# Name: 27. Remove Element


from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Pointer to track position of the next non-val element
        k = 0

        # Iterate through the array
        for i in range(len(nums)):
            # If the current element is not equal to val, we keep it
            if nums[i] != val:
                # Move the non-val element to the front of the array
                nums[k] = nums[i]
                # Increment k to point to the next position
                k += 1

        # Return the number of elements not equal to val
        return k


# Taking input from the user
# Input format: comma-separated values
nums = list(map(int, input().split(",")))
val = int(input())  # Integer value to remove
print(Solution().removeElement(nums, val))
