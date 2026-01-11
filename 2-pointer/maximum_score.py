MODULO_AMT = 10**9 + 7

def maximum_score(arr1: list[int], arr2: list[int]) -> int:
    i = j = 0
    sum1 = sum2 = 0
    total = 0

    n, m = len(arr1), len(arr2)

    while i < n and j < m:
        if arr1[i] < arr2[j]:
            sum1 += arr1[i]
            i += 1
        elif arr1[i] > arr2[j]:
            sum2 += arr2[j]
            j += 1
        else:
            # common element (jump point)
            total += max(sum1, sum2) + arr1[i]
            total %= MODULO_AMT
            sum1 = sum2 = 0
            i += 1
            j += 1

    # Remaining elements
    while i < n:
        sum1 += arr1[i]
        i += 1

    while j < m:
        sum2 += arr2[j]
        j += 1

    total += max(sum1, sum2)
    return total % MODULO_AMT
