from typing import List


#DP solution
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        
        word_set = set(dictionary)
        dp = [float('inf')] * (len(s) + 1)
        dp[len(s)] = 0

        for i in range(len(s) - 1, -1, -1):
            dp[i] = dp[i + 1] + 1
            for j in range(i, len(s)):
                if s[i:j + 1] in word_set:
                    dp[i] = min(dp[i], dp[j + 1])
        
        return dp[0]
