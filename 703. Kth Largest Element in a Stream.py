from typing import List
import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHip, self.k = nums, k
        heapq.heapify(self.minHip)
        print(self.minHip)
    # def add(self, val: int) -> int:
        


# Your KthLargest object will be instantiated and called as such:
obj = KthLargest(3,[[4, 5, 8, 2], [3], [5], [10], [9], [4]])
# param_1 = obj.add(val)