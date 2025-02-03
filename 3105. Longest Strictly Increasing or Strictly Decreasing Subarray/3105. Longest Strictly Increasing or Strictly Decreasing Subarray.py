from typing import List
class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        window_length = 1
        res = 1
        for i in range(1,n):
            if nums[i-1]<nums[i]:
                window_length+=1
            else:
                window_length= 1
            res = max(res,window_length)
        window_length = 1
        for i in range(1,n):
            if nums[i-1]>nums[i]:
                window_length+=1
            else:
                window_length= 1
            res = max(res,window_length)
        return res