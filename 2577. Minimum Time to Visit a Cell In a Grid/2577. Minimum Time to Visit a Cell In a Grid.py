from typing import List
import heapq
class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        if grid[0][1]>1 or grid[1][0]>1 :
            return -1
        
        m,n = len(grid), len(grid[0])
        min_heap = [(0,0,0)]
        visited = set()

        while min_heap:
            time, row, col = heapq.heappop(min_heap)

            if (row, col) == (m-1, n-1):
                return time
            
            neibores = [(row+1,col), (row-1, col), (row, col+1), (row, col-1)]
            
            for neibore_row, neibore_col in neibores:
                
