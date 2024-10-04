from typing import List
class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        remainder = total%p

        if remainder == 0 :
            return 0
        
        res = len(nums)
        current_sum = 0
        remainder_to_index = {0:-1}
        for i, n in enumerate(nums):
            current_sum = (current_sum+n)%p
            prefix = (current_sum-remainder+p)%p
            if prefix in remainder_to_index:
                length = i -remainder_to_index[prefix]
                res= min(res, length)
            remainder_to_index[current_sum]=i
        return -1 if res== len(nums) else res