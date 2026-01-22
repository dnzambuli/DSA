def bubble_sort(arr):
    """
    1. Go through the array, one value at a time.
    
    2. For each value, compare the value with the next value.
    
    3. If the value is higher than the next one, swap the values so that the highest value comes last.
    
    4. Go through the array as many times as there are values in the array.

    
    :param arr: unsorted array
    """
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j+1], arr[j]
                swapped = True
        print(swapped)
        if not swapped:
            return 

mylist = [64, 34, 25, 12, 22, 11, 90, 5]

bubble_sort(mylist)

print(mylist)