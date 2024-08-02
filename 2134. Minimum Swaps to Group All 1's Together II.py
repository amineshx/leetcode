from typing import List
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n=len(nums)
        total_one=nums.count(1)
        left=0
        window_one=max_window_one=0
        for r in range(2*n):
            if nums[r%n]:
                window_one+=1
            if r-left+1>total_one:
                window_one-=nums[left%n]
                left+=1
            max_window_one=max(max_window_one,window_one)
        
        return total_one-max_window_one

        