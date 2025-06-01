def bubbleSort(arr):
    swapped = False
    for i in range(len(arr)):
        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:  
            # If no swap then array is sorted. So no need for comparison
            break
    return arr


arr = [5, 3, 4, 1, 2]
print("Original Array", arr)
bubbleSort(arr)
print("Sorted Array", arr)
