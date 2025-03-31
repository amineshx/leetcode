from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums)-1
        for i in reversed(range(len(nums)-1)):
            if nums[i]+i>=goal:
                goal=i 
        if goal==0:
            return True 
        return False

sol = Solution()
print(sol.canJump(nums = [2,3,1,1,4]))