from typing import List
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        def dp(n,memo):
            if n<2:
                return cost[n]
            if n in memo: return memo[n]
            memo[n]=cost[n] + min(dp(n-1,memo), dp(n-2,memo))
            return memo[n]
        
        return min(dp(len(cost)-1,memo={}),dp(len(cost)-2,memo={}))