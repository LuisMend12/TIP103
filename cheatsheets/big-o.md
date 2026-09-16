# Big O Quick Reference

## Common complexities (best to worst)

| Notation     | Name         | Example |
|--------------|--------------|---------|
| O(1)         | Constant     | array index access, hash map get/set |
| O(log n)     | Logarithmic  | binary search, balanced BST operations |
| O(n)         | Linear       | single loop over input, linear search |
| O(n log n)   | Linearithmic | efficient sorting (merge sort, heap sort) |
| O(n^2)       | Quadratic    | nested loops over the same input, bubble sort |
| O(2^n)       | Exponential  | naive recursive Fibonacci, subsets/power set |
| O(n!)        | Factorial    | brute-force permutations |

## Data structure operation costs

| Structure          | Access | Search | Insert | Delete |
|---------------------|--------|--------|--------|--------|
| Array               | O(1)   | O(n)   | O(n)*  | O(n)*  |
| Dynamic array (list)| O(1)   | O(n)   | O(1) amortized end | O(n) |
| Linked list         | O(n)   | O(n)   | O(1) at known node | O(1) at known node |
| Hash map / set      | -      | O(1) avg | O(1) avg | O(1) avg |
| Binary search tree (balanced) | O(log n) | O(log n) | O(log n) | O(log n) |
| Heap (binary)       | O(1) peek | O(n) | O(log n) | O(log n) |
| Stack / Queue       | O(1) top/front | O(n) | O(1) | O(1) |

\* insert/delete at an arbitrary index requires shifting elements.

## Rules of thumb

- Drop constants and lower-order terms: O(2n + 100) → O(n).
- Nested loops over the same input multiply: two nested loops → O(n^2).
- Loops in sequence (not nested) add, and the larger term dominates:
  O(n) + O(n^2) → O(n^2).
- A loop that halves the search space each iteration → O(log n).
- Recursion: complexity is (number of calls) × (work per call). Use the
  recurrence relation (e.g. T(n) = 2T(n/2) + O(n) → O(n log n), the merge
  sort recurrence) when calls branch.
- Space complexity counts extra space only — recursion depth counts toward
  space (call stack), even if no explicit data structure is allocated.

## Interview sanity checks by input size

Rough guide for what's fast enough at a ~10^8 operations/sec budget:

| n            | Feasible complexity |
|--------------|----------------------|
| n <= 10-12   | O(n!) / O(2^n) (backtracking, permutations) |
| n <= ~20-25  | O(2^n) (bitmask DP, subsets) |
| n <= ~500    | O(n^3) |
| n <= ~5,000  | O(n^2) |
| n <= ~10^6   | O(n log n) or O(n) |
| n <= ~10^8+  | O(log n) or O(1) |
