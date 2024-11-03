from typing import List
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_sum = float('inf')
        
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                # If the current sum is exactly the target, return it
                if current_sum == target:
                    return current_sum
                
                # Update the closest sum if the current one is closer
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                
                # Move the pointers
                if current_sum < target:
                    left += 1
                else:
                    right -= 1
        
        return closest_sum