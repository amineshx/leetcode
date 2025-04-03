from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for c in coins:  
            for i in range(c, amount + 1):  
                dp[i] = min(dp[i], dp[i - c] + 1)  

        return dp[amount] if dp[amount] != float('inf') else -1
        
sol = Solution()
print(sol.coinChange(coins = [1,2,5], amount = 11))
print(sol.coinChange(coins = [2], amount = 3))
print(sol.coinChange(coins = [1], amount = 0))