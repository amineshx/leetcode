from typing import List
class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        rows,cols=len(grid), len(grid[0])

        def DFS(r,c,visited):
            if (r<0 or c< 0 or r==rows or c==cols or
                grid[r][c]==0 or (r,c) in visited ):
                return
            visited.add((r,c))
            neighbors=[[r+1,c],[r,c+1],[r-1,c],[r,c-1]]
            for neiR, neiC in neighbors:
                DFS(neiR,neiC,visited)
        def Helper():
            visited=set()
            count=0
            for row in range(rows):
                for col in range(cols):
                    if grid[row][col] and (row,col) not in visited:
                        DFS(row,col,visited)
                        count+=1
            return count
        
        if Helper() !=1:
            return 0 
        
        for row in range(rows):
            for col in range(cols): 
                if grid[row][col]==0:
                    continue
                grid[row][col]=0
                if Helper()!=1:
                    return 1
                grid[row][col]=1
        return 2 