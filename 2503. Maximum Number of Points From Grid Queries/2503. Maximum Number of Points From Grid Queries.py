from typing import List
from heapq import heappop, heappush
class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        n,m = len(grid), len(grid[0])
        new_queries = [(q,i) for i,q in enumerate(queries)]
        new_queries.sort()
        min_heap = [(grid[0][0],0,0)]
        res = [0]*len(queries)
        points = 0
        visited = set([(0,0)])

        for query, idx in new_queries:
            while min_heap and min_heap[0][0] < query:
                _, row, col = heappop(min_heap)
                points+=1
                directions = [[1,0], [-1,0], [0,1], [0,-1]]
                for dRow, dCol in directions:
                    new_dRow, new_dCol = row+dRow, col+ dCol
                    if 0<=new_dRow<n and 0 <=new_dCol<m and (new_dRow,new_dCol) not in visited:
                        heappush(min_heap, (grid[new_dRow][new_dCol],new_dRow,new_dCol))
                        visited.add((new_dRow,new_dCol))
            res[idx]=points
        return res

