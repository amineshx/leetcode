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

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        max_prefix = nums[0]
        diff = 0 
        res = 0

        for i in range(1,len(nums)):
            res = max(res, diff*nums[i])

            max_prefix = max(max_prefix, nums[i])
            diff = max(diff, max_prefix-nums[i])
        return res