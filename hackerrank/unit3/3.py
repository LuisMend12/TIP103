import ast
import sys


def deepest_acorns(boxes):
    sums = {}

    def dfs(boxes, depth):
        for box in boxes:
            if isinstance(box, int):
                sums[depth] = sums.get(depth, 0) + box
            else:
                dfs(box, depth + 1)

    dfs(boxes, 1)

    if not sums:
        return 0

    return sums[max(sums)]

# if __name__ == '__main__':
#     _args = ast.literal_eval(sys.stdin.read().strip())
#     if not isinstance(_args, tuple):
#         _args = (_args,)
#     print(repr(deepest_acorns(*_args)))

print(deepest_acorns([3, [4, 5], 6]))  # Example test case, output should be 9
print(deepest_acorns([[1, [7]], [2, [3, [10]]], 8]))  # Example test case, output should be 8