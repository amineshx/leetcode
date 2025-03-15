from typing import List
class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def canRob(nums, mid, k):
            count = 0
            n = len(nums)
            i = 0
            while i < n:
                if nums[i] <= mid:
                    count += 1
                    i += 1
                i += 1
            return count >= k
        left, right = 1, max(nums)
        res = right
        while left <= right:
            mid = (left + right) // 2
            if canRob(nums, mid, k):
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        return res

sol = Solution()
print(sol.minCapability(nums = [2,3,5,9], k = 2))
print(sol.minCapability(nums = [2,7,9,3,1], k = 2))