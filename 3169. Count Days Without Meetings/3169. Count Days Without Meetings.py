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

class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        prev_end=0
        for start,end in meetings:
            start = max(start,prev_end+1)
            lenght = end-start+1
            days -= max(lenght,0)
            prev_end = max(prev_end,end)
        
        return days
sol = Solution()
print(sol.countDays(days = 5, meetings = [[2,4],[1,3]]))