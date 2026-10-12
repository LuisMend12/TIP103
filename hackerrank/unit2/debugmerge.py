#!/bin/python3

import math
import os
import random
import re
import sys
import ast



#
# Complete the 'merge_dicts' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY dict1
#  2. INTEGER_ARRAY dict2
#
def merge_dicts(dict1, dict2):
    merged = dict1  
    for key, value in dict2.items():
        if value not in merged:  
            merged[key] = value
    return merged
if __name__ == '__main__':
    input_data = sys.stdin.read().strip()
    input_list = ast.literal_eval(input_data)
    
    dict1 = input_list[0]
    dict2 = input_list[1]

    result = merge_dicts(dict1, dict2)
    print(result)