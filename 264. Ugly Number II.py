import heapq
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        minHeap=[1] # init the minheap with the first ugly num which is 1
        visited=set()
        prim_factors=[2,3,5]    

        for i in range(n):
            res=heapq.heappop(minHeap)
            if i == n-1:
                return res
            
            for j in  prim_factors:
                num= res*j
                if num not in visited:
                    visited.add(num)
                    heapq.heappush(minHeap,num)