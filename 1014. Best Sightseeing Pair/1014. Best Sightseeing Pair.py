from typing import List
class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        res = 0
        current_max = values[0] - 1
        for i in range(1, len(values)):
            res = max(res, values[i]+current_max)
            current_max= max(current_max-1, values[i]-1)

        return res
