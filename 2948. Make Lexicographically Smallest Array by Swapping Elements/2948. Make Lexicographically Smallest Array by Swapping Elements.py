from typing import List
from collections import deque
class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        groups = []
        num_to_group = {}

        for num in sorted(nums):
            if not groups or abs(num- groups[-1][-1])>limit:
                groups.append(deque())
            groups[-1].append(num)
            num_to_group[num]=len(groups)-1
        
        res = []
        for num in nums:
            j=num_to_group[num]
            res.append(groups[j].popleft())
        return res

sol = Solution()
print(sol.lexicographicallySmallestArray(nums = [1,5,3,9,8], limit = 2))
print(sol.lexicographicallySmallestArray(nums = [1,7,6,18,2,1], limit = 3))
print(sol.lexicographicallySmallestArray(nums = [1,7,28,19,10], limit = 3))