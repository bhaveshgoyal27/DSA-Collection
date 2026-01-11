def subarray_sum(arr: list[int], target: int) -> list[int]:
    prefix_sums = {0: 0}
    tot_sum = 0
    for i in range(len(arr)):
        tot_sum += arr[i]
        req = tot_sum - target
        if req in prefix_sums:
            return [prefix_sums.get(req), i+1]
        prefix_sums[tot_sum] = i+1
    # WRITE YOUR BRILLIANT CODE HERE
    return []