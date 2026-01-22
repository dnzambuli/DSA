def quick_sort(arr):
    """
    
    1. Choose a value in the array to be the pivot element.
    
    2. Order the rest of the array so that lower values than the pivot element are on the left, and higher values are on the right.
    
    3. Swap the pivot element with the first element of the higher values so that the pivot element lands in between the lower and higher values.
    
    4. Do the same operations (recursively) for the sub-arrays on the left and right side of the pivot element.

    
    :param arr: unsorted array
    """