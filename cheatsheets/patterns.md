# Common Interview Problem Patterns

A cheat sheet of "if the problem looks like X, reach for Y" heuristics.

## Two pointers
**Signal:** sorted array (or can be sorted), looking for a pair/triplet, or
comparing from both ends (palindrome check).
**Idea:** one pointer from each end (or a slow/fast pair) moving inward based
on a comparison, avoiding the nested-loop brute force.
**Examples:** Two Sum II (sorted), container with most water, valid palindrome,
3Sum (sort + two pointers per fixed element).

## Sliding window
**Signal:** "contiguous subarray/substring" + a size, sum, or count condition
("longest", "shortest", "at most K distinct", "contains all characters").
**Idea:** expand a right pointer, shrink a left pointer when the window
becomes invalid, track a running aggregate (sum/count/frequency map).
**Examples:** longest substring without repeating characters, minimum window
substring, max sum subarray of size k.

## Fast & slow pointers
**Signal:** linked list, cycle detection, "find the middle."
**Idea:** two pointers moving at different speeds through the same structure.
**Examples:** detect cycle in linked list (Floyd's), find middle of linked
list, find start of cycle, happy number.

## Hash map / set for lookups
**Signal:** "have I seen this before," counting frequencies, complement
lookups (X - current value).
**Idea:** trade O(n) space for turning an O(n) search into O(1).
**Examples:** Two Sum, group anagrams, longest consecutive sequence,
duplicate detection.

## Binary search
**Signal:** sorted array, or a monotonic "yes/no" condition over a range
("can we do it with capacity X?" — search over the answer).
**Idea:** repeatedly halve the search space; watch off-by-one bounds
(`lo <= hi` vs `lo < hi`, `mid = lo + (hi - lo) // 2`).
**Examples:** classic binary search, search in rotated sorted array, find
peak element, capacity to ship packages within D days (binary search on the
answer).

## BFS / DFS on trees and graphs
**Signal:** tree/graph traversal, "shortest path in unweighted graph" (BFS),
"all paths" or "connected components" (DFS), level-order processing.
**Idea:** BFS with a queue for shortest-path/level-by-level; DFS with
recursion or an explicit stack for exploring all paths/backtracking.
**Examples:** level order traversal, number of islands, course schedule
(topological sort via DFS or Kahn's/BFS), word ladder (BFS shortest path).

## Backtracking
**Signal:** "generate all," "find all combinations/permutations/subsets,"
constraint satisfaction (N-Queens, Sudoku).
**Idea:** build a partial solution, recurse, undo ("backtrack") the choice
before trying the next option. Prune early when a partial solution is
already invalid.
**Examples:** subsets, permutations, combination sum, N-Queens, word search.

## Dynamic programming
**Signal:** "count the number of ways," "minimum/maximum cost/length,"
overlapping subproblems, optimal substructure, decisions that depend on
prior decisions.
**Idea:** define state (what does dp[i] or dp[i][j] mean?), find the
recurrence relating a state to smaller subproblems, decide iterative
(bottom-up table) vs. memoized recursion (top-down).
**Examples:** climbing stairs, coin change, longest common subsequence,
knapsack, edit distance.

## Heap / priority queue
**Signal:** "top K," "kth largest/smallest," merging sorted structures,
scheduling by priority.
**Idea:** maintain a heap of size K (min-heap for "top K largest"), or a
heap of pointers/values for merging.
**Examples:** kth largest element, top K frequent elements, merge K sorted
lists, task scheduler.

## Monotonic stack
**Signal:** "next greater/smaller element," histogram/skyline problems.
**Idea:** maintain a stack that's always increasing or decreasing; pop
elements that violate the order as you scan.
**Examples:** daily temperatures, largest rectangle in histogram, next
greater element.

## Prefix sums
**Signal:** repeated range-sum queries, "subarray sum equals K."
**Idea:** precompute cumulative sums so any range sum is O(1); combine with
a hash map of prefix-sum counts for subarray-sum problems.
**Examples:** range sum query, subarray sum equals K, product of array
except self (prefix/suffix products).
