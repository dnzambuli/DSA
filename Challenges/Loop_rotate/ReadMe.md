# Initial Solution

```py
def loop_rotate(rotations: int, arr):
    n = len(arr)
    if rotations == n or rotations == 0:
        return arr
    val = n-rotations
    left =  -rotations if rotations < 0 else val
    a, b = arr[:left], arr[left:]
    a, b = b, a
    print(f"first: {a}\nlast: {b}")

    return a + b
```

## Assessment

Strengths:

✅ Handles basic rotation correctly
✅ Considers edge cases (rotation = 0, rotation = n)
✅ Attempts to handle negative rotations
✅ Uses slicing (Pythonic approach)

Issues:

❌ Doesn't handle rotations > n (e.g., rotating 7 times in array of 5)
❌ Negative rotation logic is incomplete
❌ Creates extra copies (space inefficient)
❌ Debug print statement in production code
❌ Line a, b = b, a is unnecessary (swapping then concatenating)

# Correction

```py
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

```
