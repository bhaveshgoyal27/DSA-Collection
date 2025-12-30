# Sorting algos

A stable sorting algorithm means that their relative order is maintained when two elements have the same value. For example, if we are sorting a hand of cards, we have a Seven of Hearts before a Seven of Spades in the initial hand. After a stable sort, the Seven of Hearts is still before the Seven of Spades because their values are the same. However, in an unstable algorithm, the Seven of Spades might appear before the Seven of Hearts. The above is only valid when comparing the cards by value, not by suit.

An in-place sorting algorithm means that the algorithm does not use any additional data structure to hold temporary data. Additional memory cannot be avoided (as swapping two elements requires additional memory), but it should be something like a temporary variable that uses very little extra memory.

| Algorithm        | Best Time     | Average Time  | Worst Time    | Space Complexity | Stable | In-Place |
|-----------------|--------------|---------------|---------------|------------------|--------|----------|
| Bubble Sort     | O(n)          | O(n²)         | O(n²)         | O(1)             | Yes    | Yes      |
| Selection Sort  | O(n²)         | O(n²)         | O(n²)         | O(1)             | No     | Yes      |
| Insertion Sort  | O(n)          | O(n²)         | O(n²)         | O(1)             | Yes    | Yes      |
| Merge Sort      | O(n log n)    | O(n log n)    | O(n log n)    | O(n)             | Yes    | No       |
| Quick Sort      | O(n log n)    | O(n log n)    | O(n²)         | O(log n)         | No     | Yes      |
| Heap Sort       | O(n log n)    | O(n log n)    | O(n log n)    | O(1)             | No     | Yes      |
| Counting Sort   | O(n + k)      | O(n + k)     | O(n + k)     | O(k)             | Yes    | No       |
| Radix Sort      | O(nk)         | O(nk)        | O(nk)        | O(n + k)         | Yes    | No       |
| Bucket Sort     | O(n + k)      | O(n + k)     | O(n²)        | O(n + k)         | Depends| No       |
| Shell Sort      | O(n log n)    | O(n^1.5)     | O(n²)        | O(1)             | No     | Yes      |
| Tim Sort        | O(n)          | O(n log n)   | O(n log n)   | O(n)             | Yes    | No       |

### Best overall: Merge Sort
#### Guaranteed O(n log n) in all cases; Easy to explain; Stable and predictable

### Best in practice: Quick Sort
#### Fast average case; Used in real systems

### Bubble Sort → easiest to explain
### Insertion Sort → best for nearly sorted arrays
