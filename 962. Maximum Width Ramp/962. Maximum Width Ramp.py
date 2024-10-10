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


# using monoMonotonic Stack
class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []
        max_width = 0
        
        for i in range(len(nums)):
            if not stack or nums[i] < nums[stack[-1]]:
                stack.append(i)
        
        for j in range(len(nums) - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[j]:
                i = stack.pop()
                max_width = max(max_width, j - i)
        
        return max_width

sol = Solution()
print(sol.maxWidthRamp(nums = [6,0,8,2,1,5]))