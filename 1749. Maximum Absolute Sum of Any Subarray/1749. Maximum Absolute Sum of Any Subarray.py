from typing import List
class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        min_prefix_sum = max_prefix_sum = current = res = 0

        for num in nums:
            current+=num
            res = max(res, abs(current-min_prefix_sum), abs(current-max_prefix_sum))
            max_prefix_sum = max(max_prefix_sum,current)
            min_prefix_sum = min(min_prefix_sum, current)
        return res

sol = Solution()
print(sol.maxAbsoluteSum(nums = [1,-3,2,3,-4]))
print(sol.maxAbsoluteSum(nums = [2,-5,1,-4,3,-2]))