import math
import os
import random
import re
import sys
def max_sum(arr):
    maxSum = -63
    for i in range(4):
        for j in range(4): 
            hourglass = sum(arr[i][j:j+3])+arr[i+1][j+1]+sum(arr[i+2][j:j+3])
            if hourglass > maxSum:
                maxSum = hourglass
    return maxSum

if __name__ == '__main__':
    fl = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = max_sum(arr)

    fl.write(str(result) + '\n')

    fl.close()
