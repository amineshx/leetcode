from typing import List
import heapq
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        k = len(nums)
        left= right = nums[0][0]
        min_heap = []
        for i in range(k):
            l = nums[i]
            left=min(left,l[0])
            right = max(right,l[0])
            heapq.heappush(min_heap,(l[0],i,0))
        
        res = [left,right]
        while True:
            _ ,i,index = heapq.heappop(min_heap)
            index+=1
            if index == len(nums[i]):
                break
            
            next_val = nums[i][index]
            heapq.heappush(
                min_heap,(next_val,i,index)
            )
            left = min_heap[0][0]
            right = max(right, next_val)
            if right - left < res[1]-res[0]:
                res = [left,right]
        return res
sol = Solution()
print(sol.smallestRange(nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]))