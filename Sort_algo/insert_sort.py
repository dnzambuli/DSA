def insert_sort(arr):
    """
    1. copy current smallest value

    2. shift all the largest values on the left to the right

    3. put the smallest value where the space has been made 
    
    :param arr: unsorted array 
    """
    n = len(arr)
    for i in range(1, n):
        # start by comparing the first two values 
        insert_index = i 
        current_value = arr[i]
        for j in range(i-1, -1, -1):
            # check the if left values are larger than current value
            if arr[j] > current_value:
                # move the larger values left
                arr[j + 1] = arr[j]
                # update paste position
                insert_index = j
            else:
                # there are no more larger values to the right of current_value
                break
        # paste the new smallest value 
        arr[insert_index] = current_value    

mylist = [64, 34, 25, 12, 22, 11, 90, 5]

insert_sort(mylist)

print(mylist)