def remove_duplicates(arr: list[int]) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    slow = 0
    for fast in range(len(arr)):
        if arr[slow] != arr[fast]:
            slow += 1
            arr[slow] = arr[fast]
    return slow + 1