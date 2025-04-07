from typing import List
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        dp = [1] * n
        max_size = 1
        max_index = 0

        for i in range(1, n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1

            if dp[i] > max_size:
                max_size = dp[i]
                max_index = i

        res = []
        current_num = nums[max_index]
        current_size = max_size

        for i in range(max_index, -1, -1):
            if current_num % nums[i] == 0 and dp[i] == current_size:
                res.append(nums[i])
                current_num = nums[i]
                current_size -= 1

        res.reverse()
        return res