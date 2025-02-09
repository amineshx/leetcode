from typing import List
class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        freq = {}
        good_pairs = 0

        for i, num in enumerate(nums):
            key = num - i
            good_pairs += freq.get(key, 0)
            freq[key] = freq.get(key, 0) + 1

        n = len(nums)
        return (n * (n - 1)) // 2 - good_pairs

sol = Solution()
print(sol.countBadPairs(nums = [4,1,3,3]))
print(sol.countBadPairs(nums = [1,2,3,4,5]))