from typing import List
class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        res = 0
        def isPrefixAndSuffix(str1: str, str2: str):
            if str2.startswith(str1) and str2.endswith(str1):
                return True
        
        for i in range(len(words)-1):
            j=i+1
            while j<len(words):
                if isPrefixAndSuffix(words[i], words[j]):
                    res+=1
                j+=1
        return res

sol = Solution()
print(sol.countPrefixSuffixPairs(words = ["a","aba","ababa","aa"]))