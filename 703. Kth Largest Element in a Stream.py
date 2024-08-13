from typing import List
import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHip, self.k = nums, k
        heapq.heapify(self.minHip)
        while len(self.minHip)>k:
            heapq.heappop(self.minHip)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHip, val)
        if len(self.minHip)>self.k:
            heapq.heappop(self.minHip)
        return self.minHip[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)