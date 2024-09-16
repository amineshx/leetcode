from typing import List
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints.sort()
        
        res = (
            24*60 - self.get_time(timePoints[-1])+self.get_time(timePoints[0])
        )
        for i in range(len(timePoints)-1):
            cur = self.get_time(timePoints[i+1])
            prev = self.get_time(timePoints[i])
            diff = cur-prev
            res = min(res,diff)
        return res
    
    def get_time(self,t):
        HH,MM=map(int,t.split(":"))

        return 60*HH + MM
