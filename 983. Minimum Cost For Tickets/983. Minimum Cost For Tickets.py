from typing import List
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0] * (len(days)+1)

        for i in reversed(range(len(days))):
            j=i
            dp[i]=float("inf")
            for cost, duariation in zip(costs,[1,7,30]):
                while j< len(days) and days[j]< days[i]+duariation:
                    j+=1
                dp[i] = min(dp[i], cost+dp[j])
        return dp[0]

sol = Solution()
print(sol.mincostTickets(days = [1,4,6,7,8,20], costs = [2,7,15]))