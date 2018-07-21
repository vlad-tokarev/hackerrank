#!/bin/python3

"""
@url https://www.hackerrank.com/challenges/recursive-digit-sum/problem
"""

import math
import os
import random
import re
import sys

# Complete the superDigit function below.
# Complete the superDigit function below.
def superDigit(n, k=1):
    base = 10
    super_digit = 0

    for c in n:
        super_digit += int(c)

    super_digit = int(super_digit)

    super_digit *= k

    if super_digit < 10:
        return super_digit
    else:
        super_digit = str(super_digit)
        return superDigit(super_digit)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = nk[0]

    k = int(nk[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()