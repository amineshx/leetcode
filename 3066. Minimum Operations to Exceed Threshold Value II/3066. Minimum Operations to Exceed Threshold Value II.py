from typing import List
import bisect
from collections import deque
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        q = deque(nums)
        res=0
        while q[0]<k:
            x,y=q.popleft(),q.popleft()
            num = min(x,y) *2 + max(x,y)
            bisect.insort(q,num)
            res+=1
        return res
