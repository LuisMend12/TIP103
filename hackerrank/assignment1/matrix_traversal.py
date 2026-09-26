#!/bin/python3

import math
import os
import random
import re
import sys
import ast


#
# Complete the 'get_sum_of_odds' function below.
#
# The function is expected to return an INTEGER_ARRAY.
#

def get_sum_of_odds(matrix):
    odd_list = []
    count_odd = 0
    for row in matrix:
        for element in row:
            if element % 2 != 0:
                count_odd += 1
                odd_list.append(element)
    # Write your code here
    r = [count_odd, sum(odd_list)]
    return r

if __name__ == '__main__':
    outfile = open(os.environ['OUTPUT_PATH'], 'w')
    input_data = input()
    while (input_data != "END"):
        matrix = ast.literal_eval(input_data)

        result = get_sum_of_odds(matrix)
        outfile.write(str(result) + '\n')
        input_data = input()
    outfile.close()