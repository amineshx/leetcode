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

sol = Solution()
print(sol.minOperations(nums = [2,11,10,1,3], k = 10))
print(sol.minOperations(nums = [1,1,2,4,9], k = 20))