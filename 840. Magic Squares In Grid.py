from typing import List
class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def helper(row,col):
            vals=set()
            for i in range(row,row+3):
                for j in range(col,col+3):
                    if grid[i][j] in vals or not (1<= grid[i][j]<=9):
                        return 0
                    vals.add(grid[i][j])
            
            for i in range(row,row+3):
                if sum(grid[i][col:col+3])!=15:
                    return 0 
            
            for i in range(col,col+3):
                if (grid[row][i]+grid[row+1][i]+grid[row+2][i])!=15:
                    return 0 
            if(
                grid[row][col]+grid[row+1][col+1]+grid[row+2][col+2]!=15 or 
                grid[row][col+2]+grid[row+1][col+1]+grid[row+2][col]!=15 
            ):
                return 0
            
            return 1
        n,m=len(grid),len(grid[0])
        res=0

        for row in range(n-2):
            for col in range(m-2):
                res+=helper(row,col)
        
        return res