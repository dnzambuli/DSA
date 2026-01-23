def loop_rotate(rotations: int, arr):
    # no array or empty array 
    if not arr:
        return arr 
    n = len(arr)

    # account for rotations greater than the array length
    rots = rotations % n 

    # just return the array if it is not being rotated 
    if rots == 0:
        return arr

    # example
    # [1, 2, 3, 4, 5]
    # rotations = 2
    #       arr[-2:] -> [4, 5]
    #       arr[:-2] -> [1, 2, 3]
    # [4, 5] + [1, 2, 3]
    # 
    # rotations = -2
    #       arr[2:] -> [3, 4, 5]
    #       arr[:2] -> [1, 2]
    # [3, 4, 5] + [1, 2]

    return arr[-rots:] + arr[:-rots]

print(loop_rotate(2, [1, 2, 3, 4, 5]))