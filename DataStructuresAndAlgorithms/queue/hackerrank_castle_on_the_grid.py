#!/bin/python3

import math
import os
import random
import re
import sys

from collections import deque
# Complete the 'minimumMoves' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING_ARRAY grid
#  2. INTEGER startX
#  3. INTEGER startY
#  4. INTEGER goalX
#  5. INTEGER goalY
#

    
        


def minimumMoves(grid, startX, startY, goalX, goalY):
    visited=set()
    c=0
    que=deque([[startX,startY,c]])
    moves=[[1,0],[-1,0],[0,1],[0,-1]]
    while que:
        startX,startY,c=que.popleft()
        c+=1
        for xi,yi in moves:
            x,y=startX,startY
            while True:
                x,y=x+xi,y+yi
                if len(grid)>x>=0 and len(grid[0])>y>=0 and grid[x][y]=='.':
                    if x==goalX and y==goalY:
                        return c
                    elif (x,y) not in visited:
                        visited.add((x,y))
                        que.append([x,y,c])
                else:
                    break
    
    return -1                        
            
            
        
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    first_multiple_input = input().rstrip().split()

    startX = int(first_multiple_input[0])

    startY = int(first_multiple_input[1])

    goalX = int(first_multiple_input[2])

    goalY = int(first_multiple_input[3])

    result = minimumMoves(grid, startX, startY, goalX, goalY)

    fptr.write(str(result) + '\n')

    fptr.close()

