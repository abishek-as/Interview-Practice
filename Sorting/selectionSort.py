def selectionSort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]


arr = [5, 3, 4, 1, 2]
print("Original Array", arr)
selectionSort(arr)
print("Sorted Array", arr)
