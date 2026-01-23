def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
    lsize, rsize = len(nums1), len(nums2)
    middle = lsize + rsize

    merged_prev, merged_curr = 0, 0
    lpointer, rpointer = 0, 0
    for _ in range((middle // 2) + 1):
        # make the previously updated urrent value become this iterations previous number 
        merged_prev = merged_curr 
        # check if the pointer for num 1 is at 0 and 
        # check if any of these two is true:
        #       1. the whole nums2 has been checked (pointer on the right is >= right size)
        #       2. the number at num1[0, ...] < num2[0, ...]
        # Update the current merged value to be the smallest number (number pointed to by right pointer)
        if lpointer < lsize and (rpointer >= rsize or nums1[lpointer] < nums2[rpointer]):
            merged_curr = nums1[lpointer]
            lpointer += 1

        # if the whole right side has been checked Or,
        #       1. right has not been fully checked because NO number in nums1 > num2 numbers
        # update current to be the smallest value in nums2
        else:
            merged_curr = nums2[rpointer] 
            rpointer +=1

    if middle % 2 == 0:
        return (merged_prev + merged_curr)/2
    else:
        return float(merged_curr)
