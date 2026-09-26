#!/bin/python3

import math
import os
import random
import re
import sys
import ast



#
# Complete the 'can_place_flowers' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts following parameters:
#  1. INTEGER_ARRAY flowerbed
#  2. INTEGER n
#

def can_place_flowers(flowerbed, n):
    # Write your code here
    f = [0] + flowerbed + [0]
    
    for i in range(1, len(f) - 1):
        if f[i-1] == 0 and f[i] == 0 and f[i+1] == 0:
            f[i] = 1
            n -= 1
            
    return n <= 0        

if __name__ == '__main__':
    outfile = open(os.environ['OUTPUT_PATH'], 'w')
    input_data = sys.stdin.read().strip().splitlines()
    
    for line in input_data:
        match = re.match(r"(\[.*\]),\s*(\d+)", line)
        if match:
            flowerbed_str = match.group(1)
            n_str = match.group(2)
            
            flowerbed = ast.literal_eval(flowerbed_str)
            n = int(n_str)
            result = can_place_flowers(flowerbed, n)
            outfile.write(str(result) + '\n')
    outfile.close()