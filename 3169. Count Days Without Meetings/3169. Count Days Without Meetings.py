from typing import List

# brute force solution Time Limit Exceeded
class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        set_ther = set()
        for meet in meetings:
            start = meet[0]
            end = meet[1]
            for i in range(start,end+1):
                set_ther.add(i)
        res = 0
        for i in range(1,days+1):
            if i not in set_ther:
                set_ther.add(i)
                res+=1
        return res

sol = Solution()
print(sol.countDays(days = 5, meetings = [[2,4],[1,3]]))