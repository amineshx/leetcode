from typing import List
class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        n=len(nums)
        max_sum = nums[0]
        current_max = 0
        for i in range(1,n):
            if nums[i-1]<nums[i]:
                max_sum+=nums[i]
            else:
                current_max=max(current_max,max_sum)
                max_sum=nums[i]
        current_max=max(current_max,max_sum)
        return current_max  

sol = Solution()
print(sol.maxAscendingSum(nums = [12,17,15,13,10,11,12]))