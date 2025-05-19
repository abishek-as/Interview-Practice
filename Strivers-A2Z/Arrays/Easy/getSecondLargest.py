# Date: 2 Jan 2025
# Link: https://bit.ly/3pFvBcN
# Name: Second Largest Element in an Array without sorting

# User function Template for python3
class Solution:
    def getSecondLargest(self, arr):
        # Returns the second largest distinct element in the array, or -1 if none exists

        if len(arr) < 2:
            return -1  # Not enough elements for second largest

        largest = -1
        second_largest = -1

        for num in arr:
            if num > largest:
                # Found new largest; update second largest first
                second_largest = largest
                largest = num
            elif largest > num > second_largest:
                # Update second largest if num is between largest and second_largest
                second_largest = num

        return second_largest


sol = Solution()

print(sol.get_second_largest([12, 35, 1, 10, 34, 1]))  # Output: 34
print(sol.get_second_largest([10, 5, 10]))             # Output: 5
print(sol.get_second_largest([10, 10, 10]))            # Output: -1
