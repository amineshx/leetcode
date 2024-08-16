from typing import List
class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        mins,maxs=[min(sub_array) for sub_array in arrays], [max(sub_array) for sub_array in arrays]
        return abs(min(mins)-max(maxs))