from typing import List
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        TotalSum =  sum(nums)
        if TotalSum%2 !=0:
            return False
        
        res = TotalSum//2
        dp = [False]*(res+1)
        dp[0]=True

        for num in nums:
            for i in range(res,num-1,-1):
                dp[i]=dp[i] or dp[i-num]
        return dp[res]