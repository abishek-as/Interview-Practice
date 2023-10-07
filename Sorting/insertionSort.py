def insertionSort(array):

    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        
        # Compare key with each element on the left of it 
        # until an element smaller than it is found
        
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        
        # Place key at after the element just smaller than it.
        array[j + 1] = key

arr = [5, 3, 4, 1, 2]
print("Original Array", arr)
insertionSort(arr)
print("Sorted Array", arr)
