from typing import List
import heapq
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        n = len(classes)
        summ=0
        arr=[]
        for p,q in classes:
            summ+=p/q 
            arr.append(((p-q)/(q*(q+1)), p, q))
        heapq.heapify(arr)

        for _ in range(extraStudents):
            (r,p,q)=arr[0]
            if r==0:
                break
            summ-=r
            r2=(p-q)/((q +1.0)* (q + 2.0))
            heapq.heapreplace(arr,(r2,p+1,q+1))
        
        return summ/n

sol = Solution()
print(sol.maxAverageRatio(classes = [[1,2],[3,5],[2,2]], extraStudents = 2))