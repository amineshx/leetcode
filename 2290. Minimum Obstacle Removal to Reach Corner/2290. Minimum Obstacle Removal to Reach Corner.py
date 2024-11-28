from typing import List 
from collections import deque
class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        q = deque([(0,0,0)])
        visited = set([(0,0)])

        while q:
            obstacle, row, col = q.popleft()

            if (row,col) == (m-1, n-1):
                return obstacle
            
            neibores = [[row+1,col],[row-1, col],[row, col+1],[row, col-1]]

            for neibore_row, neibore_col in neibores:
                if (neibore_row,neibore_col) in visited or neibore_row < 0 or neibore_col <0 or neibore_row ==m or neibore_col == n:
                    continue

                if grid[neibore_row][neibore_col]:
                    q.append((obstacle+1, neibore_row, neibore_col))
                else:
                    q.appendleft((obstacle,neibore_row,neibore_col))
                visited.add((neibore_row, neibore_col))
        
sol = Solution()
print(sol.minimumObstacles(grid = [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]]))