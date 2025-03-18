from typing import List
class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        res=0
        left=0
        current=0
        for right in range(len(nums)):
            while current&nums[right]:
                current=current^nums[left]
                left+=1
            res=max(res,right-left+1)
            current=current|nums[right]
        return res