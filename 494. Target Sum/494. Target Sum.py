from typing import List
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def backtracking(i, current_sum):
            if (i, current_sum) in memo:
                return memo[(i,current_sum)]
            if i==len(nums):
                return 1 if current_sum == target else 0
            
            memo[(i,current_sum)] = (
                backtracking(i+1, current_sum+nums[i])+
                backtracking(i+1, current_sum-nums[i])
            )
            return memo[(i,current_sum)]
        
        return backtracking(0,0)