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