from typing import List
class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        res = []
        C = [0]*(n+1)
        commun = 0

        for i in range(n):
            if C[A[i]]==0:
                C[A[i]]=1
            elif C[A[i]]==1:
                commun+=1
            if C[B[i]]==0:
                C[B[i]]=1
            elif C[B[i]]==1:
                commun+=1
            res.append(commun)
        return res

sol = Solution()
print(sol.findThePrefixCommonArray(A = [1,3,2,4], B = [3,1,2,4]))