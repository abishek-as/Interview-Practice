# Date: 24 March 2025
# Link: https://leetcode.com/problems/valid-anagram/
# Name: 242. Valid Anagram


from typing import List
from collections import Counter


class Solution:
    # ✅ Approach 1: Using Hashmaps to Count Frequencies
    def isAnagram(self, s: str, t: str) -> bool:
        # Check if lengths are different (quick exit)
        if len(s) != len(t):
            return False

        # Define hashmaps to store character frequencies
        countS, countT = {}, {}

        # Count frequencies of characters in both strings
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)  # Increment count in s
            countT[t[i]] = 1 + countT.get(t[i], 0)  # Increment count in t

        # Compare frequencies of characters in both hashmaps
        for key in countS:
            if countS[key] != countT.get(key, 0):
                return False

        # Return True if all character frequencies match
        return True

    # ✅ Approach 2: Using Counter from collections
    def isAnagramCounter(self, s: str, t: str) -> bool:
        # Use Counter to count character frequencies and compare
        return Counter(s) == Counter(t)

    # ✅ Approach 3: Using Sorted Strings Comparison
    def isAnagramSorted(self, s: str, t: str) -> bool:
        # Check lengths first for efficiency
        if len(s) != len(t):
            return False

        # Sort both strings and compare them
        return sorted(s) == sorted(t)


# Create an instance of the Solution class
obj = Solution()

# Test case: Valid anagram
s = input().strip()
t = input().strip()

# Call the original approach
print(obj.isAnagram(s, t))  # Output: True

# # Call the Counter approach
# print("Using Counter:", obj.isAnagramCounter(s, t))  # Output: True

# # Call the Sorted approach
# print("Using Sorted:", obj.isAnagramSorted(s, t))  # Output: True
