from typing import List
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m,n = len(matrix),len(matrix[0])
        res=0
        visited = {}
        def DFS(row,col):
            if row==m or col==n or not matrix[row][col]:
                return 0
            if (row,col) in visited:
                return visited[(row,col)]
            
            visited[(row,col)] = 1+min(DFS(row+1,col),DFS(row,col+1),DFS(row+1,col+1))
            return visited[(row,col)]
        for row in range(m):
            for col in range(n):
                res+= DFS(row,col)
        return res        

