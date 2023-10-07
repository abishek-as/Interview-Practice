nums1 = [i**2 for i in range(10) if i % 2 == 0]  # Only if
nums2 = [i**2 if i % 2 == 0 else i**3 for i in range(10)]  # If else
nums3 = [i for i in range(50) if i % 2 == 0 if i %
         3 == 0 if i % 5 == 0]  # Multiple Ifs
nums4 = [i for i in range(50) if i % 2 == 0 and i %
         2 == 0 and i % 4 == 0]  # Multiple conditions

print("Only if:", nums1)
print("Only if-else:", nums2)
print("Multiple ifs:", nums3)
print("Multiple conditions:", nums4)
