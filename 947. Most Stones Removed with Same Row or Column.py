from typing import List

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        parent = {}
        def find(x):
            if parent.setdefault(x, x) != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        for x, y in stones:
            union(x, ~y)  

        distinct_components = len({find(x) for x in parent})
        
        return len(stones) - distinct_components
