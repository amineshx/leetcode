from typing import List
class Union:
    def __init__(self,n):
        self.parent=list(range(n))
        self.size=[1]*n
    
    def find(self,x):
        if x != self.parent[x]:
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]
    
    def union(self,x,y):
        x=self.find(x)
        y=self.find(y)
        if x!=y:
            if self.size[x]<self.size[y]:
                self.parent[x]=y
                self.size[y]+=self.size[x]
            else:
                self.parent[y]=x
                self.size[x]+=self.size[y]

class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        UF= Union(n)
        res = []
        for u,v,_ in edges:
            UF.union(u,v)
        
        coast={}
        for u,v,w in edges:
            root=UF.find(u)
            if root not in coast:
                coast[root]=w
            else:
                coast[root]&=w
        
        for source, dist in query:
            r1,r2=UF.find(source), UF.find(dist)
            if r1!=r2:
                res.append(-1)
            else:
                res.append(coast[r1])
        return res