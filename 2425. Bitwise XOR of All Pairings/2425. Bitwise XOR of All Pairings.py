from typing import List
class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        m = len(nums2)
        x = 0
        y = 0
        if n % 2 != 0:
            for i in nums2:
                y ^= i
        if m % 2 != 0:
            for i in nums1:
                x ^= i
        return x ^ y