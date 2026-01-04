import math

def container_with_most_water(arr: list[int]) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    l, r = 0, len(arr)-1
    maxVolume = -math.inf
    while l < r:
        volume = min(arr[l], arr[r]) * (r - l)
        maxVolume = max(maxVolume, volume)
        if arr[l] <= arr[r]: l += 1
        elif arr[l] > arr[r]: r -= 1
    return maxVolume