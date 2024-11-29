from typing import List
import heapq
class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        if grid[0][1]>1 and grid[1][0]>1 :
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
                if neibore_row < 0 or neibore_col <0 or neibore_row ==m or neibore_col == n or (neibore_row, neibore_col) in visited:
                    continue
                
                time_to_wait= 0
                if abs(grid[neibore_row][neibore_col]-time)%2==0:
                    time_to_wait+=1
                n_time = max(grid[neibore_row][neibore_col]+ time_to_wait, time+1)
                heapq.heappush(min_heap,(n_time,neibore_row,neibore_col))
                visited.add((neibore_row,neibore_col))
