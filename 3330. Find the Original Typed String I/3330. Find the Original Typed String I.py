class Solution:
    def possibleStringCount(self, word: str) -> int:
        res = 0
        i=0
        while i<len(word)-1:
            if word[i]==word[i+1]:
                res+=1
            i+=1
        return res+1

sol = Solution()
print(sol.possibleStringCount(word = "abbcccc"))
print(sol.possibleStringCount(word = "abcd"))
print(sol.possibleStringCount(word = "aaaa"))