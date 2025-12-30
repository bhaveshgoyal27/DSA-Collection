def merge_sort(lst):
    n = len(lst)
    if n<=1:
        return lst

    a = n - (n//2)
    l1 = merge_sort(lst[:a])
    l2 = merge_sort(lst[a:])
    l = list()

    i1, i2 = len(l1), len(l2)
    i = j = 0
    while i<i1 and j<i2:
        if l1[i]<=l2[j]:
            l.append(l1[i])
            i+=1
        else:
            l.append(l2[j])
            j+=1
    while i!=i1:
        l.append(l1[i])
        i+=1
    while j!=i2:
        l.append(l2[j])
        j+=1

    return l


lst = [5,4,1,3,2]
print(merge_sort(lst))

# Time complexity - O(N log(N))
# Space complexity - O(N)