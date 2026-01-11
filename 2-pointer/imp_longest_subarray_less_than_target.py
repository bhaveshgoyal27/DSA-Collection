def subarray_sum_longest(nums: list[int], target: int) -> int:
    ans = 0
    i = 0
    s = 0
    for j in range(len(nums)):
        while s+nums[j]>target:
            s-=nums[i]
            i+=1
        s+= nums[j]
        ans = max(ans, j-i+1)
    return ans