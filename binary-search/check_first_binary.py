def find_boundary(arr: list[bool]) -> int:
    left, right = 0, len(arr) - 1
    boundary_index = -1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid]:
            boundary_index = mid
            right = mid - 1
        else:
            left = mid + 1

    return boundary_index

### Find the first index which value is true, in a list of boolean values
### eg: [0,1,1,1,0] ans=1