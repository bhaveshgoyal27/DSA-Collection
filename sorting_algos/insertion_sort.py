def insertion_sort(lst):
    n = len(lst)
    for i in range(n):
        current = i

        while current > 0 and lst[current]< lst[current-1]:
            lst[current], lst[current-1] = lst[current-1], lst[current]
            current-=1
    return lst

lst = [5,4,1,3,2]
print(insertion_sort(lst))

# How it works
# The idea of an insertion sort is this: initially, only the first item is considered sorted.
# Then, for each item in the sequence, we "insert" that item into the sorted list by swapping it with the item
# before it until the item is smaller than the current item.

# Time complexity - O(N^2)
# Space complexity - O(1)