def find_first_occurrence(arr: list[int], target: int) -> int:
    idx = -1
    l, r = 0, len(arr)-1
    while l<=r:
        mid =(l+r)//2
        if arr[mid]< target:
            l = mid + 1
        elif arr[mid]> target:
            r = mid - 1
        else:
            idx = mid
            r = mid - 1
    return idx

# Given a sorted array of integers and a target integer, find the first occurrence of the target and return its index.
# Return -1 if the target is not in the array.
# 
# Input:
#
# arr = [1, 3, 3, 3, 3, 6, 10, 10, 10, 100]
# target = 3
# Output: 1
#
# Explanation: The first occurrence of 3 is at index 1.
#
# Input:
#
# arr = [2, 3, 5, 7, 11, 13, 17, 19]
# target = 6
# Output: -1
#
# Explanation: 6 does not exist in the array.