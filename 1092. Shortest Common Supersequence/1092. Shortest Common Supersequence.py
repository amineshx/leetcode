class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        memo = {}
        def backtracking(ch1,ch2):
            if (ch1,ch2) in memo:
                return memo[(ch1,ch2)]
            if ch1==len(str1):
                return str2[ch2:]
            if ch2==len(str2):
                return str1[ch1:]
            
            if str1[ch1]==str2[ch2]:
                return str1[ch1] + backtracking(ch1+1, ch2+1)
            
            res1=str1[ch1]+backtracking(ch1+1,ch2)
            res2=str2[ch2]+backtracking(ch1,ch2+1)        

            if len(res1)<len(res2):
                memo[(ch1,ch2)]=res1
                return res1
            memo[(ch1,ch2)]=res2
            return res2
        return backtracking(0,0)
            