from typing import List
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        res =0 
        allowed=tuple(allowed)
        for word in words:
            check=True
            for c in word:
                if c not in allowed:
                    check=False
                    break
            if check==True:
                res+=1 
        return res

sol =Solution()
print(sol.countConsistentStrings(allowed = "ab", words = ["ad","bd","aaab","baa","badab"]))