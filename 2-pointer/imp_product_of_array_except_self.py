def product_of_array_except_self(nums: list[int]) -> list[int]:
    # WRITE YOUR BRILLIANT CODE HERE
    prefix = 1
    n = len(nums)
    answer = [1]*n
    for i in range(n-1):
        answer[i+1] = prefix * nums[i]
        prefix *= nums[i]

    suffix = 1
    for i in reversed(range(n)):
        answer[i] *= suffix
        suffix *=nums[i]
    return answer
