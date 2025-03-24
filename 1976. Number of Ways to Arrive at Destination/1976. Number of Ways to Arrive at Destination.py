from typing import List
from collections import defaultdict
from heapq import heappop, heappush
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        adj = defaultdict(list)
        for u,v,t in roads:
            adj[v].append((t,u))
            adj[u].append((t,v))
        mod = 10**9 + 7
        min_heap = [(0,0)]
        min_coast = [float("inf")]*n 
        path_cnt = [0]*n
        path_cnt[0]=1

        while min_heap:
            cost,node = heappop(min_heap)
            for neib_coast, neib in adj[node]:
                if cost + neib_coast < min_coast[neib]:
                    min_coast[neib]=cost+neib_coast
                    path_cnt[neib]=path_cnt[node]
                    heappush(min_heap, (cost+neib_coast,neib))
                elif cost+neib_coast==min_coast[neib]:
                    path_cnt[neib]=(path_cnt[neib] + path_cnt[node])%mod
        
        return path_cnt[n-1]


sol = Solution()
print(sol.countPaths(n = 7, roads = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]))