from typing import List
from collections import defaultdict
# class Solution:
#     def sumPrefixScores(self, words: List[str]) -> List[int]:
#         res = []
#         count = defaultdict(int)

#         for w in words:
#             for i in range(len(w)):
#                 count[w[:i+1]]+=1
        
#         for w in words:
#             score=0
#             for i in range(len(w)):
#                 score+=count[w[:i+1]]
#             res.append(score)
#         return res


#SOL2
class PrefixNode:
    def __init__(self):
        self.children = [None]*26
        self.count = 0

class PrefixTree:
    def __init__(self):
        self.root = PrefixNode()
    
    def insert(self,w):
        cur = self.root
        for c in w :
            i = ord(c)-ord('a')
            if not cur.children[i]:
                cur.children[i]=PrefixNode()
            cur=cur.children[i]
            cur.count+=1

    def get_res(self,w):
        cur=self.root
        score=0
        for c in w:
            i=ord(c)-ord('a')
            cur = cur.children[i]
            score+=cur.count
        return score
class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        res = []
        prefix_tree = PrefixTree()

        for w in words:
            prefix_tree.insert(w)
        for w in words:
            res.append(prefix_tree.get_res(w))
        return res
sol =Solution()
print(sol.sumPrefixScores(words = ["abc","ab","bc","b"]))