def two_sum_sorted(arr: list[int], target: int) -> list[int]:
    # WRITE YOUR BRILLIANT CODE HERE
    l, r = 0, len(arr)-1
    while l < r:
        sum = arr[l] + arr[r]
        if sum < target:
            l += 1
        elif sum > target:
            r -= 1
        else:
            return [l, r]
    return []