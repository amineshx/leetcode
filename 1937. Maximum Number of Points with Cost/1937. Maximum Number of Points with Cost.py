from typing import List
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n,m=len(points),len(points[0])
        cur_row=points[0]

        for i in range(1,n):
            nxt=points[i]
            left,right=[0]*m,[0]*m
            left[0]=cur_row[0]

            for j in range(1,m):
                left[j]=max(cur_row[j],left[j-1]-1)
            right[m-1]=cur_row[m-1]
            for j in range(m-2, -1, -1):
                right[j]=max(cur_row[j], right[j+1]-1)
            for j in range(m):
                nxt[j]+=max(left[j],right[j])
            cur_row=nxt
        return max(cur_row)


sol=Solution()
print(sol.maxPoints([[0,3,0,4,2],[5,4,2,4,1],[5,0,0,5,1],[2,0,1,0,3]]))