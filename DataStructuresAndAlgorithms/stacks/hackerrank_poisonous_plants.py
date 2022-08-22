#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'poisonousPlants' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY p as parameter.
#

def poisonousPlants(p):
    # Write your code here
    stack=[]
    maxday=0
    for plant in p:
        days=0
        while stack and stack[-1][0]>=plant:
            days=max(days,stack.pop()[1])
        if stack:
            days+=1
        else:
            days=0
        
        
        maxday=max(days,maxday)
        stack.append([plant,days])
        
    return maxday
            
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    result = poisonousPlants(p)

    fptr.write(str(result) + '\n')

    fptr.close()
