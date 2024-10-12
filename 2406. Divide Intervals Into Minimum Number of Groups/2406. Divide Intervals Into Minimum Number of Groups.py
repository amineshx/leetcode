from typing import List
class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        start , end = [],[]

        for left, right in intervals:
            start.append(left)
            end.append(right)
        
        start.sort()
        end.sort()

        i,j=0,0
        res = 0
        groups = 0

        while i< len(intervals):
            if start[i]<=end[j]:
                groups+=1
                i+=1
            else:
                groups-=1
                j+=1
            
            res = max(res,groups)
        return res

sol = Solution()
print(sol.minGroups([[5,10],[6,8],[1,5],[2,3],[1,10]]))