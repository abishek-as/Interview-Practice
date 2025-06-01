# Date: 25 March 2025
# Link: https://leetcode.com/problems/longest-common-prefix/
# Name: 14. Longest Common Prefix

from typing import List


class Solution:
    # ✅ Approach 1: Vertical Scanning
    def longestCommonPrefixVertical(self, strs: List[str]) -> str:
        # Loop through each character of the first string
        for i in range(len(strs[0])):
            # Compare the current character with all other strings
            for s in strs:
                # Check if index i is out of bounds or characters don't match
                if i == len(s) or s[i] != strs[0][i]:
                    # Return the common prefix up to the point of mismatch
                    return strs[0][:i]

        # If no mismatch is found, return the first string as the prefix
        return strs[0]

    # ✅ Approach 2: Sorting and Comparing First & Last Strings
    def longestCommonPrefixSorted(self, strs: List[str]) -> str:
        # Handle edge case: If only one string is present
        if len(strs) == 1:
            return strs[0]

        # Sort the list of strings lexicographically
        strs = sorted(strs)

        # Compare the first and the last string in the sorted list
        for i in range(min(len(strs[0]), len(strs[-1]))):
            # Stop if characters don't match at the same position
            if strs[0][i] != strs[-1][i]:
                # Return the prefix up to the point of mismatch
                return strs[0][:i]

        # Return the whole first string if all characters match
        return strs[0]


# ✅ Get input from the user as a list of strings
strs = input().split(",")

# Trim spaces and strip unwanted characters
strs = [s.strip() for s in strs]

# Create an instance of the Solution class
obj = Solution()

# Call and print results for both approaches
print(obj.longestCommonPrefixVertical(strs))
# print("Using Sorting Approach:", obj.longestCommonPrefixSorted(strs))
