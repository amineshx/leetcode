from typing import List
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        
        def backtrack(i,memo):
            if i>=len(questions):
                return 0
            if i in memo : return memo[i]

            points,brainpower = questions[i]
            memo[i] = max(backtrack(i+1,memo),points+backtrack(i+1+brainpower,memo))
            return memo[i]
        
        return backtrack(0,memo={})

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n=len(questions)
        memo = {k:0 for k in range(n)}
        for i in reversed(range(n)):
            points, brainpower = questions[i]
            j = i+brainpower+1
            choose = points + (memo[j] if j < n else 0)
            skip = memo[i+1] if i+1 < n else 0 
            memo[i] = max(choose,skip)
        return memo[0]

sol = Solution()
print(sol.mostPoints(questions = [[3,2],[4,3],[4,4],[2,5]]))
print(sol.mostPoints(questions = [[1,1],[2,2],[3,3],[4,4],[5,5]]))