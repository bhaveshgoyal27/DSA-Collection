def square_root(n: int) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    l, r = 0, n
    ans = -1
    while l<=r:
        mid = (l+r)//2
        if mid*mid>n:
            r = mid -1
        elif mid*mid<n:
            ans = mid
            l = mid+1
        else:
            return mid
    return ans