from typing import List
from collections import defaultdict
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        def DFS(row,col, lable):
            if row<0 or row==n or col < 0 or col == n  or grid[row][col]!=1:
                return 0
            grid[row][col]=lable
            size = 1
            nei = [[1,0],[-1,0],[0,1],[0,-1]]
            for neiRow, neiCol in nei:
                new_neiRow , new_neiCol = neiRow+row, neiCol+col 
                size+=DFS(new_neiRow,new_neiCol,lable)
            return size
        
        
        size = defaultdict(int)
        lable = 2
        for row in range(n):
            for col in range(n):
                if grid[row][col] ==1:
                    size[lable] = DFS(row,col,lable)
                    lable+=1

        def connect(row, col):
            nei = [[1,0],[-1,0],[0,1],[0,-1]]
            visited = set()
            res = 1
            for neiRow, neiCol in nei:
                new_neiRow , new_neiCol = neiRow+row, neiCol+col 
                if not (new_neiRow<0 or new_neiCol <0 or new_neiRow==n or new_neiCol==n) and grid[new_neiRow][new_neiCol] not in visited:
                    res += size[grid[new_neiRow][new_neiCol]]
                    visited.add(grid[new_neiRow][new_neiCol])
            return res
        
        res = 0 if not size else max(size.values())

        for row in range(n):
            for col in range(n):
                if grid[row][col] ==0:
                    res = max(res, connect(row,col))
        
        return res


