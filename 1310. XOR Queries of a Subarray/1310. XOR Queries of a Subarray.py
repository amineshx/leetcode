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

# class Solution:
#     def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
#         prefix=[0]
#         for n in arr:
#             prefix.append(prefix[-1]^n)
        
#         res=[]
#         for left,right in queries:
#             res.append(
#                 prefix[left]^prefix[right+1]
#             )
#         return res


# sol3
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        for i in range(1,len(arr)):
            arr[i]^=arr[i-1]
        
        res = []
        for left,right in queries:
            total = arr[right]
            remove = 0 if left ==0 else arr[left-1]
            res.append(total^remove)
        return res
    
sol = Solution()
print(sol.xorQueries( arr = [1,3,4,8], queries = [[0,1],[1,2],[0,3],[3,3]]))