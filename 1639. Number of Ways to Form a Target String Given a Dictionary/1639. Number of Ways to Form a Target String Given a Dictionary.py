from typing import List
from collections import defaultdict
class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        modulo = 10**9 + 7      # read description

        count = defaultdict(int)
        for word in words:
            for i,w in enumerate(word):
                count[(i,w)]+=1
        
        memo = {}
        def dfs(i,k):
            if i == len(target):
                return 1
            if k == len(words[0]):
                return 0 
            if (i,k) in memo:
                return memo[(i,k)]
            
            char = target[i]
            memo[(i,k)] = dfs(i, k+1)
            memo[(i,k)] += count[(k,char)]*dfs(i+1,k+1)
            return memo[(i,k)] % modulo
        
        return dfs(0,0)

sol =Solution()
print(sol.numWays(words = ["acca","bbbb","caca"], target = "aba"))