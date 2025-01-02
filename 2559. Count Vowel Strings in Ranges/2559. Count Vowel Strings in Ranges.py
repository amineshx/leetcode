from typing import List
class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowls = set("aeiou")
        prefix = [0]*(len(words)+1)
        prev = 0

        for i, word in enumerate(words):
            if word[0] in vowls and word[-1] in vowls:
                prev+=1
            prefix[i+1] = prev
        
        res = [0]*len(queries)

        for i, querie in enumerate(queries):
            left, right = querie
            res[i] = prefix[right+1]-prefix[left]
        return res

sol = Solution()
print(sol.vowelStrings(words = ["aba","bcb","ece","aa","e"], queries = [[0,2],[1,4],[1,1]]))
print(sol.vowelStrings(words = ["a","e","i"], queries = [[0,2],[0,1],[2,2]]))
