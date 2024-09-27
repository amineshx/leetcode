from typing import List
class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        n,m=len(grid1),len(grid1[0])
        visited=set()

        def DFS(row,col):
            if row<0 or col<0 or row>=n or col>=m or (row,col) in visited or grid2[row][col]==0:
                return True
            if grid1[row][col]==0:
                return False
            visited.add((row,col))
            return DFS(row + 1, col) & DFS(row - 1, col) & DFS(row, col + 1) & DFS(row, col - 1)
        res=0
        for row in range(n):
            for col in range(m):
                if grid2[row][col] == 1 and (row, col) not in visited and DFS(row,col):
                    res+=1
        return res 