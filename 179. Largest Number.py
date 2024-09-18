from typing import List
from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        for i, num in enumerate(nums):
            nums[i] = str(num)
        
        nums = sorted(nums,key=cmp_to_key(self.compare))
        return str(int("".join(nums)))

    
    def compare(self,num1,num2):
        if num1+num2>num2+num1:
            return -1
        else:
            return 1
    