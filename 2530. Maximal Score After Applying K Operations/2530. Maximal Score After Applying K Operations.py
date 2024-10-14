from typing import List 
import heapq , math
class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        res = 0
        max_heap=[ -num for num in nums]
        heapq.heapify(max_heap)
        while k:
            num = - heapq.heappop(max_heap)
            res +=num
            k-=1
            heapq.heappush(max_heap, -math.ceil(num/3))
        
        return res

sol = Solution()
print(sol.maxKelements(nums = [10,10,10,10,10], k = 5))
