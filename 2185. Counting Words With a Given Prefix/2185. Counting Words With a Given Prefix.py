from typing import List
class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        res=0
        for word in words:
            if word.startswith(pref):
                res+=1
        
        return res

sol = Solution()
print(sol.prefixCount(words = ["pay","attention","practice","attend"], pref = "at"))