from typing import List
class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n=len(grid)
        arr= [0]*(n*n+1)
        for i in range(n):
            for j in range(n):
                arr[grid[i][j]]+=1
        print(arr)
        a=b=None
        i=1
        while (a==None or b==None) and i<len(arr):
            if arr[i]>1:
                a=i
            if arr[i]==0:
                b=i
            i+=1
        return [a,b]


sol = Solution()
print(sol.findMissingAndRepeatedValues(grid = [[1,3],[2,2]]))
print(sol.findMissingAndRepeatedValues(grid = [[9,1,7],[8,9,2],[3,4,6]]))