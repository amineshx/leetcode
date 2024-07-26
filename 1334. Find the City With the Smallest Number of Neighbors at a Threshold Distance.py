from collections import defaultdict
from typing import List
import heapq

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        adj=defaultdict(list)
        for v1,v2,dist in edges:
            adj[v1].append((v2,dist))
            adj[v2].append((v1,dist))
        
        def dijkstra(source):
            heap=[(0,source)]
            visit= set()
            while heap:
                dist,node=heapq.heappop(heap)
                if node in visit:
                    continue
                visit.add(node)
                for nei,dist2 in adj[node]:
                    nei_dist = dist+dist2
                    if nei_dist <= distanceThreshold:
                        heapq.heappush(heap,(nei_dist, nei))
            
            return len(visit)-1

        res, min_count = -1, n
        for source in range(n):
            count=dijkstra(source)
            if count<=min_count:
                res,min_count= source, count
        return res