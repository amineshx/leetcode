from typing import List
class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        total_sum=mean*(m+n)
        missing_sum=total_sum-sum(rolls)
        res=[]

        if missing_sum > 6*n or missing_sum <n:
            return []
        
        while n:
            dice = min(6,missing_sum-n+1)
            res.append(dice)
            missing_sum-= dice
            n-=1
        return res