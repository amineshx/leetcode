from typing import List
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res=0
        def flip(bit):
            if bit==1:
                return 0
            return 1
        
        def start_fliping(left):
            for i in range(left,left+3):
                nums[i]=flip(nums[i])
        
        for j in range(len(nums)-2):
            if nums[j]==0:
                start_fliping(j)
                res+=1
        if all(num == 1 for num in nums):
            return res
        
        return -1
