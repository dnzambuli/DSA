def linear_search(arr, value):
    """
    find value in array using linear search
    
    :param array: a list
    :param value: the target
    """

    for i in range(len(arr)):
        if arr[i] == value:
            return i
    return False 

mylist = [3, 7, 2, 9, 5, 1, 8, 4, 6]
# x = 4
x = 10

result = linear_search(mylist, x)

if result:
    print(f"Found {x} at index: {result}")
else:
  print("Not found") 