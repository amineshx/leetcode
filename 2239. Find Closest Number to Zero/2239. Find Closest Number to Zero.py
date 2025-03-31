from typing import List

#binary search solution
class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        nums.sort()  
        left, right = 0, len(nums) - 1        
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < 0:
                left = mid + 1  
            else:
                right = mid  

        pos = nums[left] if left < len(nums) else float('inf')
        neg = nums[left - 1] if left > 0 else float('-inf')

        return pos if abs(pos) < abs(neg) or (abs(pos) == abs(neg) and pos > neg) else neg


#sol 2
class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closest = nums[0] 
        for num in nums:
            if abs(num) < abs(closest) or (abs(num) == abs(closest) and num > closest):
                closest = num
        return closest


sol = Solution()
print(sol.findClosestNumber(nums = [-4,-2,1,4,8]))