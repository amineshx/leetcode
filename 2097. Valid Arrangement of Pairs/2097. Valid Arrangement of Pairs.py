from typing import List
from collections import defaultdict
class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        adjacency_list = defaultdict(list)
        inOutDeg = defaultdict(int)

        for start, end in pairs:
            adjacency_list[start].append(end)
            inOutDeg[start] += 1  
            inOutDeg[end] -= 1    

        startNode = pairs[0][0] 
        for node in inOutDeg:
            if inOutDeg[node] == 1:
                startNode = node
                break

        path = []
        def dfs(curr):
            while adjacency_list[curr]:
                nextNode = adjacency_list[curr].pop()
                dfs(nextNode)
                path.append((curr, nextNode))

        dfs(startNode)
        return path[::-1]

sol = Solution()
print(sol.validArrangement(pairs = [[5,1],[4,5],[11,9],[9,4]]))