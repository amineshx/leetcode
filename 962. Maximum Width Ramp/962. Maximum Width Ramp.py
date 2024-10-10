from typing import List 
class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n=len(nums)
        max_right = [0]*n
        i = n-1
        prev_max=0

        for num in reversed(nums):
            max_right[i]=max(num,prev_max)
            prev_max = max_right[i]
            i-=1
        
        res =0 
        left = 0
        for right in range(n):
            while nums[left] > max_right[right]:
                left+=1
            res = max(res,right-left)
        return res 

sol = Solution()
print(sol.maxWidthRamp(nums = [6,0,8,2,1,5]))