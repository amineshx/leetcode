from typing import List


# this solution didn't pass all test cases

class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n=len(grid[0])
        sum_lines = [sum(grid[0]),sum(grid[1])]
        j=0
        print(f"i:0 j:{j}")
        while j<n:
            sum_lines[0]-=grid[0][j]
            grid[0][j]=0
            if sum_lines[0]>sum_lines[1]:
                j+=1
            else:
                break
        while j<n:
            sum_lines[1]-=grid[1][j]
            grid[1][j]=0
            j+=1
        return max(sum_lines[0],sum_lines[1])



# sol 2
class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        
        top_prefix = grid[0]
        bottom_prefix = grid[1]
        
        for i in range(1, n):
            top_prefix[i] += top_prefix[i - 1]
            bottom_prefix[i] += bottom_prefix[i - 1]
        
        res = float('inf')
        
        for j in range(n):
            top_remaining = top_prefix[-1] - top_prefix[j]
            bottom_remaining = bottom_prefix[j - 1] if j > 0 else 0
            second_robot_score = max(top_remaining, bottom_remaining)
            res = min(res, second_robot_score)
        return res

sol = Solution()
print(sol.gridGame(grid = [[1,3,1,15],[1,3,3,1]]))