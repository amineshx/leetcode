from typing import List
class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0]*n for _ in range(m)]

        for row, col in guards:
            grid[row][col]=1
        
        for row, col in walls:
            grid[row][col]=2
        
        def mark_sell(rows,cols):
            for row in range(rows+1, m):
                if grid[row][cols] in [1,2]:
                    break
                grid[row][cols]=3
            
            for row in reversed(range(0,rows)):
                if grid[row][cols] in [1,2]:
                    break
                grid[row][cols]=3
            
            for col in range(cols +1, n):
                if grid[rows][col] in [1,2]:
                    break
                grid[rows][col]=3
            
            for col in reversed(range(0,cols)):
                if grid[rows][col] in [1,2]:
                    break
                grid[rows][col]=3
        
        for r,c in guards:
            mark_sell(r,c)
        
        res = 0
        for row in grid:
            for n in row:
                if n==0:
                    res+=1
        return res