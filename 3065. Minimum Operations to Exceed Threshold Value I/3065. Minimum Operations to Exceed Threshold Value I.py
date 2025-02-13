from typing import List
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (right + left) // 2
            if nums[mid] < k:
                left = mid + 1  
            else:
                right = mid - 1  
        
        return left  

sol = Solution()
print(sol.minOperations(nums = [1, 1, 2, 4, 9], k = 9))  
