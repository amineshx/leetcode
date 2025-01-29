from typing import List
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parents = [i for i in range(n+1)]
        rank = [1]*(n+1)

        def find(node):
            if node != parents[node]:
                parents[node]= find(parents[node])
            return parents[node]
        
        def union_find(node1, node2):
            p1,p2 = find(node1),find(node2)
            if p1==p2:
                return False

            if rank[p1]>rank[p2]:
                parents[p2]=p1
                rank[p1]+=rank[p2]
            else:
                parents[p1]=p2
                rank[p2]+=rank[p1]
            return True
        
        for node1,node2 in edges:
            if not union_find(node1,node2):
                return [node1,node2]

sol = Solution()
print(sol.findRedundantConnection(edges = [[1,2],[1,3],[2,3]]))
print(sol.findRedundantConnection(edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]))