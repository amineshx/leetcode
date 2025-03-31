from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        dp=[0]*n
        dp[0]=nums[0]
        dp[1]=max(nums[0],nums[1])

        for i in range(2,n):
            dp[i]=max(dp[i-1],dp[i-2]+nums[i])
        
        return dp[n-1]

sol = Solution()
print(sol.rob(nums = [1,2,3,1]))
print(sol.rob(nums = [2,7,9,3,1]))