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

sol = Solution()
print(sol.queryResults(limit = 4, queries = [[1,4],[2,5],[1,3],[3,4]]))
print(sol.queryResults(limit = 4, queries = [[0,1],[1,2],[2,2],[3,4],[4,5]]))