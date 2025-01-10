from typing import List
class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        
        return [word for word in words1 if all(c in word for c in words2)]
        

sol = Solution()
print(sol.wordSubsets(words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["e","o"]))