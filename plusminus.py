#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    count1 = 0
    count2 = 0
    count3 = 0
    for i in range(len(arr)):
        if arr[i]>0:
            count1 = count1+1
        if arr[i]<0:
            count2 = count2 + 1
        if arr[i]==0:
            count3 = count3+1
        avgplus = count1/(len(arr))
    avgmin = count2/(len(arr))
    avgz = count3/(len(arr))
    return avgplus,avgmin,avgz


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    a, b, c = plusMinus(arr)
    print("{:.6f}".format(a));
    print("{:.6f}".format(b));
    print("{:.6f}".format(c));
