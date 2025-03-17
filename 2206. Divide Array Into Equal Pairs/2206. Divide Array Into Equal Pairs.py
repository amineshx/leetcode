from typing import List
from collections import Counter
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        hash_map = Counter(nums)
        for val in hash_map:
            if hash_map[val]%2==1:return False
        return True

sol = Solution()
print(sol.divideArray(nums = [3,2,3,2,2,2]))