# You're building a "gear loadout" screen for a game where a player owns a set of distinct items, and any combination of them (including none) is a valid loadout. Given a list of distinct integers nums, return all possible subsets (the power set). The solution set must not contain duplicate subsets.

def subsets(nums):
    res = []

    def backtrack(start, subset):
        res.append(subset.copy())
        for i in range(start, len(nums)):
            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()

    backtrack(0, [])
    return res

# Example Usage

print(subsets([1, 2, 3]))
# Example Output:

# [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]