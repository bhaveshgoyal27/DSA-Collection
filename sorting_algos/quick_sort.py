def sort_list_interval(unsorted_list, start, end):
    # If segment is 1 or 0, it's sorted
    if end - start <= 1:
        return

    # Using last element as the pivot
    pivot = unsorted_list[end - 1]
    start_ptr, end_ptr = start, end - 1

    # Partitioning process
    while start_ptr < end_ptr:
        # Find the next element from the left that is larger than the pivot
        while unsorted_list[start_ptr] < pivot and start_ptr < end_ptr:
            start_ptr += 1

        # Find the next element from the right that is smaller than or equal to the pivot
        while unsorted_list[end_ptr] >= pivot and start_ptr < end_ptr:
            end_ptr -= 1

        # Swap if pointers haven't met
        unsorted_list[start_ptr], unsorted_list[end_ptr] = unsorted_list[end_ptr], unsorted_list[start_ptr]

    # Place pivot in its final position
    unsorted_list[start_ptr], unsorted_list[end - 1] = unsorted_list[end - 1], unsorted_list[start_ptr]

    # Sort left and right of the pivot
    sort_list_interval(unsorted_list, start, start_ptr)
    sort_list_interval(unsorted_list, start_ptr + 1, end)

def quick_sort(unsorted_list: list[int]) :
    sort_list_interval(unsorted_list, 0, len(unsorted_list))
    return unsorted_list

lst = [5,4,1,3,2]
print(quick_sort(lst))

# Time complexity - O(N^2)
# Space complexity - O(N)

# How it works
# 2 pointer concept
# Select a pivot element from the list (the choice can be arbitrary).
# Rearrange the elements so that everything less than the pivot is on its left,
# and everything greater than or equal to the pivot is on its right.
# The pivot is now in its final sorted position.
# Recursively apply the same process to the sublists on the left and right of the pivot.