"""
Problem: Two Sum (LeetCode #1)

Approach:
    Single pass with a hash map from value -> index. For each number, check
    whether its complement (target - num) has already been seen; if so we
    have our pair. This avoids the O(n^2) brute-force nested loop.

Time complexity:  O(n) — one pass, O(1) average dict lookups
Space complexity: O(n) — hash map can hold up to n entries
"""

from typing import List


def solve(nums: List[int], target: int) -> List[int]:
    seen = {}  # value -> index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    raise ValueError("No two sum solution exists")


if __name__ == "__main__":
    print(solve([2, 7, 11, 15], 9))  # [0, 1]
    print(solve([3, 2, 4], 6))       # [1, 2]
