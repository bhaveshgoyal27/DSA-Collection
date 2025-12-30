def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(n-i-1):
            if lst[j]>lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst


lst = [5,4,1,3,2]
print(bubble_sort(lst))

# How it works
# Start at the beginning of the list.
# Compare the first two elements.
# Swap them if the first is bigger than the second.
# Move to the next pair and repeat.
# After each pass, the largest unsorted value “bubbles up” to the end.

# Time complexity - O(N^2)
# Space complexity - O(1)
