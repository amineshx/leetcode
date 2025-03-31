from typing import List

#memo
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        def dp(n,memo):
            if n<2:
                return cost[n]
            if n in memo: return memo[n]
            memo[n]=cost[n] + min(dp(n-1,memo), dp(n-2,memo))
            return memo[n]
        
        return min(dp(len(cost)-1,memo={}),dp(len(cost)-2,memo={}))

#tabulation
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        dp=[0]*n 
        dp[0]=cost[0]
        dp[1]=cost[1]

        for i in range(2,n):
            dp[i]=cost[i]+min(dp[i-1],dp[i-2])
        return min(dp[n-1],dp[n-2])

# liniar sol
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev2, prev1 = cost[0], cost[1]
        
        for i in range(2, len(cost)):
            curr = cost[i] + min(prev1, prev2)
            prev2, prev1 = prev1, curr

        return min(prev1, prev2)



sol = Solution()
print(sol.minCostClimbingStairs([10, 15, 20]))  # Output: 15
print(sol.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))  # Output: 6
