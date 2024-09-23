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

#DP solution2
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        word_set = set(dictionary)
        dp={ len(s):0 }

        def DFS(i):
            if i in dp:
                return dp[i]
            
            res = 1+ DFS(i+1)
            for j in range(i,len(s)):
                if s[i:j+1] in word_set:
                    res = min(res, DFS(j+1))
            dp[i]=res
            return res
        
        return DFS(0)
    

#trie solution3
class TrieNode:
    def __init__(self):
        self.children={}
        self.word=False

class Trie:
    def __init__(self,words):
        self.root=TrieNode()
        for w in words:
            curr =self.root
            for c in w :
                if c not in curr.children:
                    curr.children[c]=TrieNode()
                curr=curr.children[c]
            curr.word=True
        
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        word_set = set(dictionary)
        dp={ len(s):0 }

        def DFS(i):
            if i in dp:
                return dp[i]
            
            res = 1+ DFS(i+1)
            for j in range(i,len(s)):
                
            dp[i]=res
            return res
        
        return DFS(0)