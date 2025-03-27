from typing import List
class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        D1_grid = [val for row in grid for val in row]
        D1_grid.sort()
        diffrence = []
        for val in D1_grid:
            diff = abs(val-D1_grid[0])%x
            diffrence.append(diff)
        for diff in diffrence:
            if diff!=0:
                return -1
        median = D1_grid[len(D1_grid)//2]
        res = 0
        for val in D1_grid:
            res+=abs(val-median)//x
        return res

sol = Solution()
print(sol.minOperations(grid = [[2,4],[6,8]], x = 2))
print(sol.minOperations(grid = [[1,5],[2,3]], x = 1))
print(sol.minOperations(grid = [[1,2],[3,4]], x = 2))