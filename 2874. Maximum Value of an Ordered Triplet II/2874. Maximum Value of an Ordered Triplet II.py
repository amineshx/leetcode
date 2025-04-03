from typing import List

# O(n^2) 
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        res = 0
        left = nums[0]
        for j in range(1,len(nums)-1):
            if left<nums[j]:
                left=nums[j]
                continue
            for k in range(j+1,len(nums)):
                op = (left-nums[j])*nums[k]
                res = max(op,res)
        return res
