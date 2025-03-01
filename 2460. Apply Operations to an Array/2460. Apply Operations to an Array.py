from typing import List
class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                nums[i]*=2
                nums[i+1]=0
        
        non_zero_i=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[non_zero_i],nums[i]=nums[i],nums[non_zero_i]
                non_zero_i+=1
        return nums

sol = Solution()
print(sol.applyOperations(nums = [1,2,2,1,1,0]))