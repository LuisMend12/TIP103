#!/bin/python

import math
import os
import random
import re
import sys
import ast
from collections import deque


#
# Complete the 'longest_subarray' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY nums
#  2. INTEGER limit
#

def longest_subarray(nums, limit):
    max_q = deque()
    min_q = deque()
    left = 0
    longest = 0

    for right in range(len(nums)):
        while max_q and nums[max_q[-1]] < nums[right]:
            max_q.pop()
        max_q.append(right)

        while min_q and nums[min_q[-1]] > nums[right]:
            min_q.pop()
        min_q.append(right)

        while nums[max_q[0]] - nums[min_q[0]] > limit:
            left += 1

            if max_q[0] < left:
                max_q.popleft()
            if min_q[0] < left:
                min_q.popleft()

        longest = max(longest, right - left + 1)

    return longest   

# if __name__ == '__main__':
#     outfile = open(os.environ['OUTPUT_PATH'], 'w')
#     input_data = sys.stdin.read().strip().splitlines()
    
#     results = []
    
#     for line in input_data:
#         nums, limit = eval(line)
#         result = longest_subarray(nums, limit)
#         results.append(result)
    
#     for res in results:
#         outfile.write(str(res) + '\n')
#     outfile.close()

print(longest_subarray([8, 2, 4, 7], 4))  # Example test case


