def binary_search(sorted_arr, value):
    """
    The Binary Search algorithm works by checking the value in the center of the array. If the target value is lower, the next value to check is in the center of the left half of the array. This way of searching means that the search area is always half of the previous search area, and this is why the Binary Search algorithm is so fast.
    
    :param sorted_arr: sorted array
    :param value: the target
    """
    left, right = 0, len(sorted_arr) -1

    while left <= right:
        middle = (right + left)// 2
        if sorted_arr[middle] == value:
            return middle
        if value < sorted_arr[middle]:
            right = middle- 1
        else:
            left = middle +1
    return False 


mylist = [3, 7, 2, 9, 5, 1, 8, 4, 6]

mylist = sorted(mylist)

x = 4
# x = 10

result = binary_search(mylist, x)

if result:
    print(f"Found {x} at index: {result}")
else:
  print("Not found") 
