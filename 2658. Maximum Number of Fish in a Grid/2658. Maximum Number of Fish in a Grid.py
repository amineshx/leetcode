from typing import List
class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        def DFS(row,col):
            if (row<0 or row==n or col<0 or col==m or visited[row][col]==1) or grid[row][col]==0:
                return 0
            visited[row][col]=1
            diractions = [[1,0],[-1,0],[0,1],[0,-1]]
            res=grid[row][col]
            for drow,dcol in diractions:
                new_dr,new_dc = drow+row, dcol+col 
                res+=DFS(new_dr,new_dc)
            return res
        
        n,m = len(grid),len(grid[0])
        res = 0
        visited = [[-1]*m for _ in range(n)]
        for row in range(n):
            for col in range(m):
                if grid[row][col] or visited[row][col]==-1:
                    res=max(DFS(row,col),res)
        return res

sol = Solution()
print(sol.findMaxFish(grid = [[0,2,1,0],[4,0,0,3],[1,0,0,4],[0,3,2,0]]))
print(sol.findMaxFish(grid = [[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,1]]))