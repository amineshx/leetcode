from typing import List
from collections import defaultdict, Counter
class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        res = []
        count_words2 = defaultdict(int)
        for word in words2:
            count_word = Counter(word)   
            for c, count in count_word.items():
                count_words2[c] = max(count,count_words2[c])     
        
        for word in words1:
            count_word = Counter(word)
            check = True
            for char, count in count_words2.items():

                if count_word[char] < count:
                    check = False
                    break
            if check:
                res.append(word)
        
        return res
        

sol = Solution()
print(sol.wordSubsets(words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["e","o","e"]))