from typing import List
class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        n,m = len(mat), len(mat[0])
        position={}

        for row in range(n):
            for col in range(m):
                position[mat[row][col]] = (row,col)
        
        count_rows=[0]*n
        count_cols=[0]*m 

        for i in range(len(arr)):
            row, col = position[arr[i]]
            count_rows[row]+=1
            count_cols[col]+=1

            if count_rows[row]==m or count_cols[col]==n :
                return i
        

sol = Solution()
print(sol.firstCompleteIndex(arr = [1,3,4,2], mat = [[1,4],[2,3]]))
print(sol.firstCompleteIndex(arr = [1,4,5,2,6,3], mat = [[4,3,5],[1,2,6]]))
print(sol.firstCompleteIndex(arr = [2,8,7,4,1,3,5,6,9], mat = [[3,2,5],[1,4,6],[8,7,9]]))