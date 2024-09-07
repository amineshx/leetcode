from typing import List
from collections import deque,defaultdict
class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        adj=defaultdict(list)
        for v1,v2 in edges:
            adj[v1].append(v2)
            adj[v2].append(v1)
        q=deque([1])
        current_time=0
        res =-1
        visit_times=defaultdict(list)   
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node ==n:
                    if res !=-1:
                        return current_time
                    res = current_time
                for nei in adj[node]:
                    nei_times=visit_times[nei]
                    if len(nei_times)==0 or (len(nei_times)==1 and nei_times[0]!=current_time):
                        q.append(nei)
                        nei_times.append(current_time)
            if(current_time//change)%2==1:
                current_time+=change-(current_time%change)
            current_time+=time

sol = Solution()
print(sol.secondMinimum(n = 5, edges = [[1,2],[1,3],[1,4],[3,4],[4,5]], time = 3, change = 5))
