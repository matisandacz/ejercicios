#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'maxima_diferencia' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY nums as parameter.
#

def countingSort(arr):
    upperBound = 10000
    count = [0] * (upperBound)
    for num in arr:
        count[num] += 1
    res = []
    for elem in range(upperBound):
        for _ in range(count[elem]):
            res.append(elem)
    return res
        

def maxima_diferencia(nums):
    sortedNums = countingSort(nums)
    maxDiff = 0
    for i in range(len(sortedNums) - 1):
        maxDiff = max(maxDiff, sortedNums[i+1] - sortedNums[i])
    return maxDiff
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nums = [int(x) for x in input().split(" ")]

    result = maxima_diferencia(nums)

    fptr.write(str(result) + '\n')

    fptr.close()
