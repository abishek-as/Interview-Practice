# Date: 1 Jan 2025
# Link: https://bit.ly/3Pld280
# Name: Largest Element in Array

class Solution:
    def find_largest_element(self, array):
        # Initialize the largest element with the first element of the array
        largest_element = array[0]

        # Iterate through each element in the array
        for index in range(len(array)):
            current_element = array[index]

            # Update the largest element if a bigger element is found
            if current_element > largest_element:
                largest_element = current_element

        # Return the largest element found in the array
        return largest_element


sol = Solution()
print(sol.find_largest_element([10, 20, 4]))       # Output: 20
print(sol.find_largest_element([20, 10, 20, 4, 100]))  # Output: 100
