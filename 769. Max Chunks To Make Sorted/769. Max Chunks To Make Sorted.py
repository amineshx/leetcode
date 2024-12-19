from typing import List
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        current_max = -1
        res=0
        for i, num in enumerate(arr):
            current_max=max(num, current_max)

            if current_max==i:
                res+=1
        return res

sol = Solution()
print(sol.maxChunksToSorted(arr = [4,3,2,1,0]))