#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'truckTour' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY petrolpumps as parameter.
#





def truckTour(petrolpumps):
    global n
    # Write your code here
    c_petrol=list(map(lambda x:x[0]-x[1],petrolpumps))
    capacity=n
    for i in range(capacity):
        if not i<0:
            j=start=i
            pumps_trav=0
            for _ in range(capacity):
                pumps_trav+=c_petrol[j]
                if pumps_trav<0:
                    break
                j=(j+1)%capacity
            else:
                return start
                
                
                
                
                
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())
    petrolpumps = []
    
    for _ in range(n):
        petrolpumps.append(list(map(int, input().rstrip().split())))

    result = truckTour(petrolpumps)

    fptr.write(str(result) + '\n')

    fptr.close()
