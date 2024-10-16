import heapq
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res , maxHeap = "", []
        for count,c in [(-a,"a"),(-b,"b"),(-c,"c")]:
            if count !=0:
                heapq.heappush(maxHeap,(count,c))
        
        while maxHeap:
            count,c  = heapq.heappop(maxHeap)

            if len(res)>1 and res[-1] == res[-2] ==c:
                if not maxHeap:
                    break

                count2,c2 =heapq.heappop(maxHeap)
                res+=c2 
                count2+=1
                if count2:
                    heapq.heappush(maxHeap,(count2,c2))
            
            else:
                res+=c
                count+=1
            if count:
                heapq.heappush(maxHeap, (count,c))
        return res