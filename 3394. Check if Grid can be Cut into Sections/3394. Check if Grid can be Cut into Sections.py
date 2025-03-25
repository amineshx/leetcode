from typing import List
class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        x = [(i[0],i[2]) for i in rectangles]
        y = [(i[1],i[3]) for i in rectangles]

        x.sort()
        y.sort()

        def count(intervals):
            cnt = 0
            prev_end=-1
            for start,end in intervals:
                if prev_end <=start:
                    cnt+=1
                prev_end=max(prev_end,end)
            return cnt 
        
        return max(count(x),count(y))>=3

sol = Solution()
print(sol.checkValidCuts(n = 5, rectangles = [[1,0,5,2],[0,2,2,4],[3,2,5,3],[0,4,4,5]]))
print(sol.checkValidCuts(n = 4, rectangles = [[0,0,1,1],[2,0,3,4],[0,2,2,3],[3,0,4,3]]))
print(sol.checkValidCuts(n = 4, rectangles = [[0,2,2,4],[1,0,3,2],[2,2,3,4],[3,0,4,2],[3,2,4,4]]))