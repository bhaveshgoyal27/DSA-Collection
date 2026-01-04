def move_zeros(nums: list[int]) -> None:
    # WRITE YOUR BRILLIANT CODE HERE

    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1
            