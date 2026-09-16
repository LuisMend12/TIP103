# Christopher Robin set up a scavenger hunt for Pooh, but it's a blustery day and several hidden clues have blown away. Write a function find_missing_clues() to help Christopher Robin figure out which clues he needs to remake. The function accepts two integers lower and upper and a unique integer array clues. All elements in clues are within the inclusive range [lower, upper].

# A clue x is considered missing if x is in the range [lower, upper] and x is not in clues.

# Return the shortest sorted list of ranges that exactly covers all the missing numbers. That is, no element of clues is included in any of the ranges, and each missing number is covered by one of the ranges.

# def find_missing_clues(clues, lower, upper):
# 	pass
# Example Usage:

# clues = [0, 1, 3, 50, 75]
# lower = 0
# upper = 99
# find_missing_clues(clues, lower, upper)

# clues = [-1]
# lower = -1
# upper = -1
# find_missing_clues(clues, lower, upper)
# Example Output:

# [[2, 2], [4, 49], [51, 74], [76, 99]]
# []

def find_missing_clues(clues, lower, upper):
    clues_set = set(clues)
    missing_ranges = []
    start = None

    for num in range(lower, upper + 1):
        if num not in clues_set:
            if start is None:
                start = num
        else:
            if start is not None:
                missing_ranges.append([start, num - 1])
                start = None

    if start is not None:
        missing_ranges.append([start, upper])

    return missing_ranges