from typing import List

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        res = []
        for start, end in queries:
            subres = 0  
            for i in range(start, end + 1):
                subres ^= arr[i]
            res.append(subres)
        return res
