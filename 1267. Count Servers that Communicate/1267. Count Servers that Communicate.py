from typing import List
class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])

        row_count = [0]*m
        col_count = [0]*n 

        for row in range(m):
            for col in range(n):
                if grid[row][col]==1:
                    row_count[row]+=1
                    col_count[col]+=1
        
        res = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] and max(row_count[row],col_count[col]) > 1:
                    res+=1
        return res