from typing import List
# sol 1 
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

# sol2 
class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n=len(nums)
        window_lenght = 1
        res = 1
        increasing = 0
        for i in range(1,n):
            if nums[i-1]<nums[i]:
                if increasing>0:
                    window_lenght+=1
                else:
                    window_lenght=2
                    increasing=1
            elif nums[i-1]>nums[i]:
                if increasing < 0:
                    window_lenght+=1
                else:
                    window_lenght=2
                    increasing=-1
            else:
                window_lenght=1
                increasing=0
            res = max(res,window_lenght)
        return res