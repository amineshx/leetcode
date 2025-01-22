from typing import List
from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n,m=len(mat),len(mat[0])
        q = deque()

        for row in range(n):
            for col in range(m):
                if mat[row][col] == 0:
                    q.append((row,col))
                else :
                    mat[row][col]=-1
        
        neighbors = [(0,1), (0,-1), (1,0), (-1,0)]
        while q:
            row, col = q.popleft()
            hight = mat[row][col]
            for nr, nc in neighbors:
                nrow , ncol = row+nr , col + nc
                if (nrow<0 or nrow==n or ncol<0 or ncol==m or mat[nrow][ncol]!=-1):
                    continue
                q.append((nrow,ncol))
                mat[nrow][ncol]=hight+1
        return mat

sol =Solution()
print(sol.updateMatrix(mat = [[0,0,0],[0,1,0],[1,1,1]]))