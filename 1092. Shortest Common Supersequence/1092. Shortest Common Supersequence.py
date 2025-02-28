# sol1 memory time execeeded
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

       # DP solution 
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m, n = len(str1), len(str2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i-1] == str2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        i, j = m, n
        result = []
        
        while i > 0 and j > 0:
            if str1[i-1] == str2[j-1]:
                result.append(str1[i-1])
                i -= 1
                j -= 1
            elif dp[i-1][j] > dp[i][j-1]:
                result.append(str1[i-1])
                i -= 1
            else:
                result.append(str2[j-1])
                j -= 1
        
        while i > 0:
            result.append(str1[i-1])
            i -= 1
        
        while j > 0:
            result.append(str2[j-1])
            j -= 1
        
        return ''.join(result[::-1])

sol = Solution()
print(sol.shortestCommonSupersequence(str1 = "abac", str2 = "cab"))
print(sol.shortestCommonSupersequence(str1 = "aaaaaaaa", str2 = "aaaaaaaa"))