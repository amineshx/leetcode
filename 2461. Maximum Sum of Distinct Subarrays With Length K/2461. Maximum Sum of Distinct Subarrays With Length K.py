from typing import List
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left, summ, res = 0, 0, 0
        current_window = set()
        
        for right in range(n):
            while nums[right] in current_window:
                current_window.remove(nums[left])
                summ -= nums[left]
                left += 1
            
            current_window.add(nums[right])
            summ += nums[right]
            
            if right - left + 1 == k:
                res = max(res, summ)
                current_window.remove(nums[left])
                summ -= nums[left]
                left += 1
        
        return res
            

sol =Solution()
print(sol.maximumSubarraySum(nums =[1,1,1,7,8,9], k = 3))