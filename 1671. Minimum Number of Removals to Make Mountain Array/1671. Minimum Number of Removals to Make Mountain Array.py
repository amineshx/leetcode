from typing import List
from bisect import bisect_left
class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        
        lis = [1] * n
        temp = []
        for i in range(n):
            pos = bisect_left(temp, nums[i])
            if pos < len(temp):
                temp[pos] = nums[i]
            else:
                temp.append(nums[i])
            lis[i] = pos + 1
        lds = [1] * n
        temp = []
        for i in range(n - 1, -1, -1):
            pos = bisect_left(temp, nums[i])
            if pos < len(temp):
                temp[pos] = nums[i]
            else:
                temp.append(nums[i])
            lds[i] = pos + 1

        max_mountain_len = 0
        for i in range(1, n - 1):
            if lis[i] > 1 and lds[i] > 1: 
                max_mountain_len = max(max_mountain_len, lis[i] + lds[i] - 1)

        return n - max_mountain_len