from typing import List
from collections import defaultdict
# Union find solution 
class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        rank = [0] * n
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            if root_x == root_y:
                return
            if rank[root_x] < rank[root_y]:
                parent[root_x] = root_y
            elif rank[root_x] > rank[root_y]:
                parent[root_y] = root_x
            else:
                parent[root_y] = root_x
                rank[root_x] += 1
        
        for u, v in edges:
            union(u, v)
        
        component_vertices = {}
        component_edges = {}
        
        for i in range(n):
            root = find(i)
            if root not in component_vertices:
                component_vertices[root] = set()
                component_edges[root] = 0
            component_vertices[root].add(i)
        
        for u, v in edges:
            root = find(u)
            component_edges[root] += 1
        
        complete_count = 0
        for root in component_vertices:
            num_vertices = len(component_vertices[root])

            expected_edges = num_vertices * (num_vertices - 1) // 2
            
            if component_edges[root] == expected_edges:
                complete_count += 1
        
        return complete_count


#sol2 DFS

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        def dfs(vortex, res):
            if vortex in visited:
                return
            visited.add(vortex)
            res.append(vortex)

            for nei in adj[vortex]:
                dfs(nei,res)
            return res
        
        adj = defaultdict(list)
        for vortex1, vortex2 in edges:
            adj[vortex1].append(vortex2)
            adj[vortex2].append(vortex1)       

        res = 0
        visited = set()
        for v in range(n):
            if v in visited:
                continue
            component = dfs(v,[])
            if all([len(component)-1 == len(adj[vort]) for vort in component]): 
                res+=1
        
        return res


sol = Solution()
print(sol.countCompleteComponents(n = 6, edges = [[0,1],[0,2],[1,2],[3,4]]))
print(sol.countCompleteComponents(n = 6, edges = [[0,1],[0,2],[1,2],[3,4],[3,5]]))
