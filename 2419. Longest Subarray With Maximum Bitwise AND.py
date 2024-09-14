from typing import List
# class Solution:
#     def longestSubarray(self, nums: List[int]) -> int:
#         target = max(nums)
#         size,res = 0,0
#         for n in nums:
#             if n == target:
#                 size+=1
#             else:
#                 size=0
#             res = max(res,size)
#         return res
    


#sol 2
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        size,res = 0,0
        current_max = 0

        for n in nums:
            if n>current_max:
                current_max=n
                size=1
                res=0
            elif n==current_max:
                size+=1
            else:
                size=0
            res = max(res,size)
        return res