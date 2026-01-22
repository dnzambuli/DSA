def selection_sort(arr):
    """
    
    1. Go through the array to find the lowest value.
    
    2. Move the lowest value to the front of the unsorted part of the array.
    
    3. Go through the array again as many times as there are values in the array.

    
    :param arr: unsorted array 
    """
    n = len(arr)
    for i in range(n -1):
        smallest_no_idx = i 
        for j in range(i + 1, n):
            if arr[j] < arr[smallest_no_idx]:
                smallest_no_idx = j # update the smallest number index
        arr[i], arr[smallest_no_idx] = arr[smallest_no_idx], arr[i] # switch the current smallest number with the new smallest number 
    return 

mylist = [64, 34, 25, 12, 22, 11, 90, 5]

selection_sort(mylist)

print(mylist)