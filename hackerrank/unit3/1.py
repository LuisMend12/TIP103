import ast
from os import times
import sys

from sympy import limit


def microwave_order(times, limit):
    order = []
    remaining = []

    for i in range(len(times)):
        if times[i] <= limit:
            order.append(i)
        else:
            remaining.append(i)

    return order + remaining


print(microwave_order([30, 90, 20], 60))
print(microwave_order([120, 60], 60))

# if __name__ == '__main__':
#     _args = ast.literal_eval(sys.stdin.read().strip())
#     if not isinstance(_args, tuple):
#         _args = (_args,)
#     print(repr(microwave_order(*_args)))
