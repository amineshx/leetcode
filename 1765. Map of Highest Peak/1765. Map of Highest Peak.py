from typing import List
from collections import deque
class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        n,m = len(isWater), len(isWater[0])
        q= deque()
        res = [[-1]*m for _ in range(n)]

        for row in range(n):
            for col in range(m):
                if isWater[row][col]==1:
                    q.append((row,col))
                    res[row][col]=0

        while q:
            row, col = q.popleft()
            hight = res[row][col]

            neighbores = [[row+1,col],[row,col+1],[row-1,col],[row,col-1]]
            for rowNei, colNei in neighbores:
                if (rowNei<0 or colNei<0 or rowNei==n or colNei==m or res[rowNei][colNei]!=-1):
                    continue
                q.append((rowNei,colNei))
                res[rowNei][colNei]=hight+1
        
        return res


sol = Solution()
print(sol.highestPeak(isWater = [[0,1],[0,0]]))
print(sol.highestPeak(isWater = [[0,0,1],[1,0,0],[0,0,0]]))