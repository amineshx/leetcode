from typing import List
class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        rows1,cols1=len(grid), len(grid[0])
        rows2,cols2=3*rows1, 3*cols1
        grid2=[[0]*cols2 for _ in range(rows2)]
        
        def DFS(r,c, visited):
            if(r<0 or c<0 or r==rows2 or c==cols2 or grid2[r][c]!=0 or (r,c) in visited):
                return
            visited.add((r,c))
            neighbors=[[r+1,c],[r,c+1],[r-1,c],[r,c-1]]
            for nr, nc in neighbors:
                DFS(nr,nc,visited)
        for row in range(rows1):
            for col in range(cols1):
                row2,col2=row*3, col*3
                if grid[row][col]=='/':
                    grid2[row2][col2+2]=1
                    grid2[row2+1][col2+1]=1
                    grid2[row2+2][col2]=1

                elif grid[row][col]=='\\':
                    grid2[row2][col2]=1
                    grid2[row2+1][col2+1]=1
                    grid2[row2+2][col2+2]=1
                    
        visited = set()
        res=0
        for r in range(rows2):
            for c in range(cols2):
                if grid2[r][c]==0 and (r,c) not in visited:
                    DFS(r,c,visited)
                    res+=1
        return res
res=Solution()
print(res.regionsBySlashes(grid = [" /","/ "]))