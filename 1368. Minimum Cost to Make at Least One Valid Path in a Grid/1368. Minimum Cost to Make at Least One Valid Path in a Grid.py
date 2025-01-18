from typing import List
from collections import deque
class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        directions = {
            1:[0,1],
            2:[0,-1],
            3:[1,0],
            4:[-1,0]
        }
        n,m=len(grid),len(grid[0])
        q=deque([(0,0,0)])
        min_coast={(0,0):0}

        while q:
            row,col, coast= q.popleft()
            if (row,col)  == (n-1,m-1):
                return coast
            
            for direction in directions:
                drow, dcol = directions[direction]
                nrow, ncol = row+drow, col+dcol
                n_coast = coast if direction == grid[row][col] else coast+1

                if (nrow<0 or ncol < 0 or nrow==n or ncol==m or n_coast >= min_coast.get((nrow,ncol),float('inf'))):
                    continue
                min_coast[(nrow,ncol)]=n_coast
                if direction == grid[row][col]:
                    q.appendleft((nrow,ncol,n_coast))
                else:
                    q.append((nrow,ncol,n_coast))