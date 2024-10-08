from typing import List
from collections import defaultdict,Counter
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        count  =defaultdict(int)

        for w in s1.split(" ") + s2.split(" "):
            count[w] +=1
        
        res =[]
        for w , cnt in count.items():
            if cnt ==1:
                res.append(w)
        return res

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        count = Counter(s1.split(" ") + s2.split(" "))
        return [w for w,cnt in count.items() if cnt == 1]

sol = Solution()
print(sol.uncommonFromSentences(s1 = "this apple is sweet", s2 = "this apple is sour"))