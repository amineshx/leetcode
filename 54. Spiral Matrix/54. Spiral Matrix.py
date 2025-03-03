from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        n,m = len(matrix), len(matrix[0])
        res = []
        left,top = 0,0
        right,bottom = m-1 , n-1 

        while left<= right and top<=bottom:

            for i in range(left,right+1):
                res.append(matrix[top][i])
            top+=1

            for i in range(top,bottom+1):
                res.append(matrix[i][right])
            right-=1

            if top <= bottom:
                for i in reversed(range(left, right + 1)):
                    res.append(matrix[bottom][i])
                bottom -= 1
            
            if left<=right:
                for i in reversed(range(top, bottom+1)):
                    res.append(matrix[i][left])
                left+=1
        
        return res
