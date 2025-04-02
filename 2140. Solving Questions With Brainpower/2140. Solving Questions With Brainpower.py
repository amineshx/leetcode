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