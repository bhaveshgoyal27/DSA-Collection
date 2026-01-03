def find_min_rotated(arr: list[int]) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    l, r = 0, len(arr)-1
    res = arr[0]
    pos = 0

    while l<=r:
        if arr[l]<=arr[r]:
            if res<arr[l]:
                return pos
            elif arr[l]<res:
                return l
            else:
                return min(pos, l)
        mid = (l+r)//2
        if res>arr[mid]:
            res = arr[mid]
            pos = mid
        elif res == arr[mid]:
            pos = min(pos, mid)
        if arr[l]<=arr[mid]:
            l = mid + 1
        else:
            r = mid - 1
    return pos

print(find_min_rotated([100,200, 300, 400, 500, 1, 10, 20 , 30 , 40, 50 , 60, 70, 80, 90]))