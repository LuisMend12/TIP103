#!/bin/python3

import math
import os
import random
import re
import sys
import ast
import json



#
# Complete the 'array_rank_transform' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def array_rank_transform(arr):
    # Write your code here
    if not arr:
        return []

    # Create a sorted list of unique elements
    sorted_unique = sorted(set(arr))
    # Create a dictionary to map each unique element to its rank
    rank_dict = {value: index + 1 for index, value in enumerate(sorted_unique)}

    # Transform the original array to ranks
    return [rank_dict[x] for x in arr]

if __name__ == '__main__':
    outfile = open(os.environ['OUTPUT_PATH'], 'w')
    input_lines = sys.stdin.read().strip().split('\n')
    
    for line in input_lines:
        if line:  # Check if the line is not empty
            arr = json.loads(line)  # Parse the line as JSON
            result = array_rank_transform(arr)
            outfile.write(str(result) + '\n')
    outfile.close()