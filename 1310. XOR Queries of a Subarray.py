from typing import List

# class Solution:
#     def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
#         res = []
#         for start, end in queries:
#             subres = 0  
#             for i in range(start, end + 1):
#                 subres ^= arr[i]
#             res.append(subres)
#         return res


# sol2

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix=[0]
        for n in arr:
            prefix.append(prefix[-1]^n)
        
        res=[]
        for left,right in queries:
            res.append(
                prefix[left]^prefix[right+1]
            )
        return res