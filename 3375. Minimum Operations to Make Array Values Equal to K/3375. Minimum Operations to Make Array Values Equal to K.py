from typing import List
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if k>min(nums):
            return -1
        
        uniq_nums = set(nums)
        if k in uniq_nums:
            return len(uniq_nums)-1
        else:
            return len(uniq_nums)