from typing import List
from collections import defaultdict
class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        n = len(queries)
        res = [0]*n 
        hash_map = {}
        color_dict = defaultdict(int)
        i=0
        for ball,col in queries:
            if ball in hash_map:
                c0 = hash_map[ball]
                color_dict[c0]-=1
                if  color_dict[c0] ==0:
                    color_dict.pop(c0)
            hash_map[ball]=col
            color_dict[col]+=1
            res[i]=len(color_dict)
            i+=1
        return res