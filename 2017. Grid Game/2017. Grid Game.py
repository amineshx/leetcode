from typing import List
class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n=len(grid[0])
        print(n)
        sum_lines = [sum(grid[0]),sum(grid[1])]
        print(sum_lines)
        j=0
        print(f"i:0 j:{j}")
        while j<n:
            sum_lines[0]-=grid[0][j]
            print(f"sum_lines[0]: {sum_lines[0]}")
            grid[0][j]=0
            print(grid)
            if sum_lines[0]>sum_lines[1]:
                j+=1
            else:
                break
        
        while j<n:
            sum_lines[1]-=grid[1][j]
            print(f"sum_lines[1]: {sum_lines[1]}")
            grid[1][j]=0
            print(grid)
            j+=1
            print(f"i:1 j:{j}")

        return max(sum_lines[0],sum_lines[1])

sol = Solution()
print(sol.gridGame(grid = [[1,3,1,15],[1,3,3,1]]))


