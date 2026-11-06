
def combination_sum(candidates, target):
    res = []
    comb = []

    def backtrack(start):
        if sum(comb) == target:
            res.append(comb.copy())
            return

        if sum(comb) > target:
            return

        for i in range(start, len(candidates)):
            comb.append(candidates[i])
            backtrack(i)
            comb.pop()

    backtrack(0)
    return res


print(combination_sum([2, 3, 6, 7], 7))
# [[2, 2, 3], [7]]
