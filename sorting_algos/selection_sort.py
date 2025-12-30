def selection_sort(lst):
    n = len(lst)
    for i in range(n):
        pos = i
        for j in range(i+1, n):
            if lst[j]<lst[pos]:
                pos = j
        lst[i], lst[pos] = lst[pos], lst[i]
    return lst

lst = [5,4,1,3,2]
print(selection_sort(lst))

# How it works
# You repeatedly find the smallest number of the list and swap it with the ith position

# Time complexity - O(N^2)
# Space complexity - O(1)