from typing import List
class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        bit_counts = [0] * 24
        for num in candidates:
            for i in range(24):
                if num & (1 << i):  
                    bit_counts[i] += 1

        return max(bit_counts)