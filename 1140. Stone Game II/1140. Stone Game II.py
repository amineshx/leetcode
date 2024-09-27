from typing import List
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        cach ={}

        def DFS(alice,i,M):
            if i== len(piles):
                return 0
            if (alice,i,M) in cach:
                return cach[(alice,i,M)]
            
            res=0 if alice else float('inf')
            total=0
            for X in range(1,2*M+1):
                if X+i>len(piles):
                    break
                total+=piles[i+X-1]
                if alice:
                    res=max(res, total+DFS(not alice,i+X,max(M,X)))
                else:
                    res=min(res, DFS(not alice,i+X,max(M,X)))
            cach[(alice,i,M)]=res
            return res
        
        return DFS(True,0,1)