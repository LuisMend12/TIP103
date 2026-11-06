# You're building a "gear loadout" screen for a game where a player owns a set of distinct items, and any combination of them (including none) is a valid loadout. Given a list of distinct integers nums, return all possible subsets (the power set). The solution set must not contain duplicate subsets.

def subsets(nums):
    res = []
    def backtrack():
        

        copy = 

    for nums in subsets(nums):

    return res

# Example Usage

print(subsets([1, 2, 3]))
# Example Output:

# [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]