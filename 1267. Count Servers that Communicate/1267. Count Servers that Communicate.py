from typing import List
# bruteforce solution
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

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        res = 0
        for row in range(m):
            row_sum = sum(grid[row])
            if row_sum<=1:
                continue
            res+=row_sum

            for col in range(n):
                if grid[row][col]:
                    grid[row][col]=-1

        for col in range(n):
            col_sum = 0
            unmarcked = 0
            for row in range(m):
                col_sum+=abs(grid[row][col])
                if grid[row][col]>0:
                    unmarcked+=1
                elif grid[row][col]<0:
                    grid[row][col]=1
            if col_sum>=2:
                res+=unmarcked
        return res

sol = Solution()
print(sol.countServers(grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]))