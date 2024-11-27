from typing import List
from collections import deque
class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        adjacency_list = [[i+1] for i in range(n)]

        def BFS():
            q = deque()
            q.append((0,0))
            visited = set()
            visited.add((0,0))
            while q:
                current, length = q.popleft()
                if current == n-1:
                    return length
                
                for neighbore in adjacency_list[current]:
                    if neighbore not in visited:
                        q.append((neighbore,length+1))
                        visited.add(neighbore)
        res = []
        for source, dist in queries:
            adjacency_list[source].append(dist)
            res.append(BFS())
        return res