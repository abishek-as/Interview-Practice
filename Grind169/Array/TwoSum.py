class Solution:
    def twoSum(self, nums: int, target: int) -> int:
        numMap = {}  # Create an empty dictionary to store values and their indices
        n = len(nums)  # Get the length of the array

        for i in range(n):  # Iterate through the list
            complement = target - nums[i]  # Calculate the complement

            if complement in numMap:
                # If the complement exists in the dictionary, return its index and the current index
                return [numMap[complement], i]

            # Add the current number and its index to the dictionary
            numMap[nums[i]] = i

        return (
            []
            # This line is just a fallback (not actually needed because the problem guarantees one solution)
        )


obj = Solution()
nums = list(map(int, input().split(",")))
target = int(input())
print(obj.twoSum(nums, target))
