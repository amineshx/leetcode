from typing import List
from bisect import bisect_left, bisect_right
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        res = 0
        n = len(nums)
        
        for i in range(n):
            left_bound = bisect_left(nums, lower - nums[i], i + 1, n)
            right_bound = bisect_right(nums, upper - nums[i], i + 1, n)
            res += (right_bound - left_bound)
        
        return res

sol = Solution()
print(sol.countFairPairs(nums=[0, 1, 7, 4, 4, 5], lower=3, upper=6))
