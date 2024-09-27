from typing import List
from collections import defaultdict
import heapq
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj=defaultdict(list)
        for i in range(len(edges)):
            src,dist=edges[i]
            adj[src].append([dist,succProb[i]])
            adj[dist].append([src,succProb[i]])

        pq=[(-1,start_node)]           # a priority queue set to -1 cuz we gonna use a max heap
        visited=set()

        while pq:
            prob,cur=heapq.heappop(pq)
            visited.add(cur)

            if cur==end_node:
                return prob*-1
            for nei, edgeProba in adj[cur]:
                if nei not in visited:
                    heapq.heappush(pq,(prob*edgeProba,nei))
        return 0

sol = Solution()
print(sol.maxProbability(n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start_node = 0, end_node = 2))