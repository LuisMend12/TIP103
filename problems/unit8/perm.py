# A DJ wants to hear every possible ordering of a short playlist before committing to one. Given a list of distinct integers nums, return all possible permutations (every ordering of the full list). You may return the answer in any order.

def permute(nums):
    res = []
    n = len(nums)

    def backtrack(perm):
        if len(perm) == n:
            res.append(perm.copy())
            return

        for a in nums:
            if a not in perm:
                perm.append(a)
                backtrack(perm)
                perm.pop()
    backtrack([])
    return res

# Example Usage

print(permute([1, 2, 3]))
# Example Output:

# [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]